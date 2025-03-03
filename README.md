
# Website on Ecs instances

This project contains two stacks, a network stack, and a server stack. The purpose of this project is to show understanding of the AWS CDK & resources that can be launched using it. Listed below are the stacks and the resources inside of them.

## Network Stack (cdk_assignment_stack.py)
- One public and one private subnet in one AZ
- One public and one private subnet in a different AZ

## Server Stack (cdk_server_stack.py)
- One EC2 webserver launched in each of the public subnets 
- An RDS instance with MYSQL engine with all private subnets as its subnet group
- A security group for the web server that opens port 80 from anywhere 
- A security group for the RDS instance that opens port 3306 to the web server security group



### CDK Instructions
To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
