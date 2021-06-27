# REST-Automation


### This framework would be used to validate REST APIs based on response code

This framework could be used to test the REST APIs by adding the APIs details in below YAML file.

```bash
config/Project_config.yaml
```

##### Details
For demonstration, we had created two Sample APIs which will be copied during Docker container creations.   

Note: As part of Next step we will be adding dynamic params in the requests  

#### Environment

```bash
1. Python 2.7.*
2. Docker
3. Operation System: Linux/ Ubuntu
```

#### Pre-Requisite

Setup your Python virtual environment by executing below command from project root dir.

```bash 
pip install requirements.txt
```

#### Execution

1. Execute below command from OS terminal after re-directing to root directory of projects

```bash
python test_controller.py
```

