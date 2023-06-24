#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_stack.unstop_stack import UnstopStack

app = cdk.App()

UnstopStack(
    app,
    "UnstopCDKStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
)

app.synth()

