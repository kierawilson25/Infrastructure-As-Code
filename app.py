#!/usr/bin/env python3
import os

import aws_cdk as cdk



from cdk_assignment.cdk_assignment_stack import CdkAssignmentStack
from cdk_assignment.cdk_server_stack import CdkServerStack

app = cdk.App()

# Instantiate the network stack
network_stack = CdkAssignmentStack(app, "CdkAssignmentStack")

# Pass the VPC from the network stack to the server stack
server_stack = CdkServerStack(app, "CdkServerStack", network_stack_vpc=network_stack.vpc)

app.synth()
