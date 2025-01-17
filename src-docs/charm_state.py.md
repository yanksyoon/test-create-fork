<!-- markdownlint-disable -->

<a href="../src/charm_state.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `charm_state.py`
State of the Charm. 

**Global Variables**
---------------
- **ARCHITECTURES_ARM64**
- **ARCHITECTURES_X86**
- **OPENSTACK_CLOUDS_YAML_CONFIG_NAME**
- **COS_AGENT_INTEGRATION_NAME**
- **DEBUG_SSH_INTEGRATION_NAME**

---

<a href="../src/charm_state.py#L85"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `parse_github_path`

```python
parse_github_path(path_str: str, runner_group: str) → GithubOrg | GithubRepo
```

Parse GitHub path. 



**Args:**
 
 - <b>`path_str`</b>:  GitHub path in string format. 
 - <b>`runner_group`</b>:  Runner group name for GitHub organization. If the path is  a repository this argument is ignored. 

**Returns:**
 GithubPath object representing the GitHub repository, or the GitHub organization with runner group information. 


---

## <kbd>class</kbd> `Arch`
Supported system architectures. 





---

## <kbd>class</kbd> `CharmConfig`
General charm configuration. 

Some charm configurations are grouped into other configuration models. 



**Attributes:**
 
 - <b>`path`</b>:  GitHub repository path in the format '<owner>/<repo>', or the GitHub organization  name. 
 - <b>`token`</b>:  GitHub personal access token for GitHub API. 
 - <b>`reconcile_interval`</b>:  Time between each reconciliation of runners. 
 - <b>`denylist`</b>:  List of IPv4 to block the runners from accessing. 
 - <b>`dockerhub_mirror`</b>:  Private docker registry as dockerhub mirror for the runners to use. 
 - <b>`openstack_clouds_yaml`</b>:  The openstack clouds.yaml configuration. 




---

<a href="../src/charm_state.py#L280"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `check_fields`

```python
check_fields(values: dict) → dict
```

Validate the general charm configuration. 



**Args:**
 
 - <b>`values`</b>:  Values in the pydantic model. 



**Returns:**
 Modified values in the pydantic model. 

---

<a href="../src/charm_state.py#L220"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_charm`

```python
from_charm(charm: CharmBase) → CharmConfig
```

Initialize the config from charm. 



**Args:**
 
 - <b>`charm`</b>:  The charm instance. 



**Returns:**
 Current config of the charm. 


---

## <kbd>class</kbd> `CharmConfigInvalidError`
Raised when charm config is invalid. 



**Attributes:**
 
 - <b>`msg`</b>:  Explanation of the error. 

<a href="../src/charm_state.py#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(msg: str)
```

Initialize a new instance of the CharmConfigInvalidError exception. 



**Args:**
 
 - <b>`msg`</b>:  Explanation of the error. 





---

## <kbd>class</kbd> `CharmState`
The charm state. 



**Attributes:**
 
 - <b>`arch`</b>:  The underlying compute architecture, i.e. x86_64, amd64, arm64/aarch64. 
 - <b>`charm_config`</b>:  Configuration of the juju charm. 
 - <b>`is_metrics_logging_available`</b>:  Whether the charm is able to issue metrics. 
 - <b>`proxy_config`</b>:  Proxy-related configuration. 
 - <b>`ssh_debug_connections`</b>:  SSH debug connections configuration information. 




---

<a href="../src/charm_state.py#L573"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_charm`

```python
from_charm(charm: CharmBase) → CharmState
```

Initialize the state from charm. 



**Args:**
 
 - <b>`charm`</b>:  The charm instance. 



**Returns:**
 Current state of the charm. 


---

## <kbd>class</kbd> `GithubOrg`
Represent GitHub organization. 



**Attributes:**
 
 - <b>`org`</b>:  Name of the GitHub organization. 
 - <b>`group`</b>:  Runner group to spawn the runners in. 




---

<a href="../src/charm_state.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `path`

```python
path() → str
```

Return a string representing the path. 



**Returns:**
  Path to the GitHub entity. 


---

## <kbd>class</kbd> `GithubRepo`
Represent GitHub repository. 



**Attributes:**
 
 - <b>`owner`</b>:  Owner of the GitHub repository. 
 - <b>`repo`</b>:  Name of the GitHub repository. 




---

<a href="../src/charm_state.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `path`

```python
path() → str
```

Return a string representing the path. 



**Returns:**
  Path to the GitHub entity. 


---

## <kbd>class</kbd> `ProxyConfig`
Proxy configuration. 



**Attributes:**
 
 - <b>`http`</b>:  HTTP proxy address. 
 - <b>`https`</b>:  HTTPS proxy address. 
 - <b>`no_proxy`</b>:  Comma-separated list of hosts that should not be proxied. 
 - <b>`use_aproxy`</b>:  Whether aproxy should be used for the runners. 


---

#### <kbd>property</kbd> aproxy_address

Return the aproxy address. 



---

<a href="../src/charm_state.py#L440"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `check_fields`

```python
check_fields(values: dict) → dict
```

Validate the proxy configuration. 



**Args:**
 
 - <b>`values`</b>:  Values in the pydantic model. 



**Returns:**
 Modified values in the pydantic model. 

---

<a href="../src/charm_state.py#L402"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_charm`

```python
from_charm(charm: CharmBase) → ProxyConfig
```

Initialize the proxy config from charm. 



**Args:**
 
 - <b>`charm`</b>:  The charm instance. 



**Returns:**
 Current proxy config of the charm. 


---

## <kbd>class</kbd> `RunnerCharmConfig`
Runner configurations for the charm. 



**Attributes:**
 
 - <b>`virtual_machines`</b>:  Number of virtual machine-based runner to spawn. 
 - <b>`virtual_machine_resources`</b>:  Hardware resource used by one virtual machine for a runner. 
 - <b>`runner_storage`</b>:  Storage to be used as disk for the runner. 




---

<a href="../src/charm_state.py#L354"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `check_fields`

```python
check_fields(values: dict) → dict
```

Validate the runner configuration. 



**Args:**
 
 - <b>`values`</b>:  Values in the pydantic model. 



**Returns:**
 Modified values in the pydantic model. 

---

<a href="../src/charm_state.py#L317"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_charm`

```python
from_charm(charm: CharmBase) → RunnerCharmConfig
```

Initialize the config from charm. 



**Args:**
 
 - <b>`charm`</b>:  The charm instance. 



**Returns:**
 Current config of the charm. 


---

## <kbd>class</kbd> `RunnerStorage`
Supported storage as runner disk. 





---

## <kbd>class</kbd> `SSHDebugConnection`
SSH connection information for debug workflow. 



**Attributes:**
 
 - <b>`host`</b>:  The SSH relay server host IP address inside the VPN. 
 - <b>`port`</b>:  The SSH relay server port. 
 - <b>`rsa_fingerprint`</b>:  The host SSH server public RSA key fingerprint. 
 - <b>`ed25519_fingerprint`</b>:  The host SSH server public ed25519 key fingerprint. 




---

<a href="../src/charm_state.py#L520"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_charm`

```python
from_charm(charm: CharmBase) → list['SSHDebugConnection']
```

Initialize the SSHDebugInfo from charm relation data. 



**Args:**
 
 - <b>`charm`</b>:  The charm instance. 


---

## <kbd>class</kbd> `UnsupportedArchitectureError`
Raised when given machine charm architecture is unsupported. 



**Attributes:**
 
 - <b>`arch`</b>:  The current machine architecture. 

<a href="../src/charm_state.py#L477"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(arch: str) → None
```

Initialize a new instance of the CharmConfigInvalidError exception. 



**Args:**
 
 - <b>`arch`</b>:  The current machine architecture. 





---

## <kbd>class</kbd> `VirtualMachineResources`
Virtual machine resource configuration. 



**Attributes:**
 
 - <b>`cpu`</b>:  Number of vCPU for the virtual machine. 
 - <b>`memory`</b>:  Amount of memory for the virtual machine. 
 - <b>`disk`</b>:  Amount of disk for the virtual machine. 





