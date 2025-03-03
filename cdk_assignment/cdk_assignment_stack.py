#Network Stack
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkAssignmentStack(Stack):
    
    @property
    def vpc(self):
        return self.network_stack_vpc

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.network_stack_vpc = ec2.Vpc(
                self, "cdk_lab_vpc", 
                ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
                max_azs=2,
                subnet_configuration=[
                    ec2.SubnetConfiguration(
                        name="PublicSubnet",
                        subnet_type=ec2.SubnetType.PUBLIC
                    ),
                        ec2.SubnetConfiguration(
                        name="PrivateSubnet",
                        subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT
                    )
                ]
        )

        # The code that defines your stack goes here
        
        # need to make a VPC inorder to have public and private subnets

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkAssignmentQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
