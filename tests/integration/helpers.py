# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Utilities for integration test."""

import json
from typing import Any

from juju.unit import Unit

from runner import Runner
from runner_manager import RunnerManager
from utilities import retry


async def remove_runner_bin(unit: Unit):
    """Remove runner binary."""
    action = await unit.run(f"rm {RunnerManager.runner_bin_path}")
    await action.wait()

    # No file should exists under with the filename.
    action = await unit.run(f"test -f {RunnerManager.runner_bin_path}")
    await action.wait()
    assert action.results["return-code"] != 0


async def check_resource_lxd_profile(unit: Unit, configs: dict[str, Any]):
    """Check for LXD profile of the matching resource config.

    Args:
        unit: Unit instance to check for the LXD profile.
        configs: Configs of the application.

    Raises:
        AssertionError: Unable to find a LXD profile with matching resource
            config.
    """
    resource_profile_name = Runner._get_resource_profile_name(
        configs["vm-cpu"]["value"], configs["vm-memory"]["value"], configs["vm-disk"]["value"]
    )

    action = await unit.run("lxc profile list --format json")
    await action.wait()
    assert action.results["return-code"] == 0
    profiles = json.loads(action.results["stdout"])
    profile_names = [profile["name"] for profile in profiles]
    assert resource_profile_name in profile_names


@retry(tries=30, delay=30)
async def check_runner_instance(unit: Unit, num: int) -> None:
    """Check if runner instances are ready.

    Args:
      app: Application instance to check the runners.
      num: Number of runner instances to check for.

    Raises:
        AssertionError: Correct number of runners is not found within timeout
            limit.
    """
    action = await unit.run("lxc list --format json")
    await action.wait()
    assert action.status == "completed"

    assert action.results["return-code"] == 0

    lxc_instance = json.loads(action.results["stdout"])
    assert len(lxc_instance) == num

    for instance in lxc_instance:
        action = await unit.run(f"lxc exec {instance['name']} -- ps aux")
        await action.wait()
        assert action.status == "completed"

        assert f"/bin/bash {Runner.runner_script}" in action.results["stdout"]