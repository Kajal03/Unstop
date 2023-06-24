# Unstop CDK APP

## Setup Instructions

### Install AWS CDK:

```
npm install -g aws-cdk@latest
```

### Add Config:

```
export CDK_DEFAULT_ACCOUNT="[YOUR_AWS_ACCOUNT_ID]"
export CDK_DEFAULT_REGION="ap-south-1"
```

### Configure Credentials:

Note: Make sure to get `AccessKeyID` and `SecretKey` from IAM User

```
aws configure
```

### Setup virtual env & install requirements:

```
cd BackendCDK
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Deploy CDK App to AWS account

Note - Make sure you are in virtual environment by running: `source .venv/bin/activate`

`cdk bootstrap` needs to be run only the first time

```
cdk bootstrap
cdk synth
cdk deploy
```

Test if all changes deployed successfully.
Git commit push. Have Fun.


## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
