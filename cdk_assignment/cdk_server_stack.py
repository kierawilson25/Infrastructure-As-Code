#NServer Stack
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_rds as rds,
    # aws_sqs as sqs,
)

import aws_cdk as cdk

from constructs import Construct

class CdkServerStack(Stack):
    
    @property
    def vpc(self):
        return self.network_stack_vpc

    def __init__(self, scope: Construct, construct_id: str, network_stack_vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        
        #create a web server's security group that opens port 80 from anywhere
        web_server_sg = ec2.SecurityGroup(
            self, "webServerSG",
            vpc=network_stack_vpc,
            description="allow HTTP traffic",
            allow_all_outbound=True #TODO: find out if this is what the default should be in our assignment
        )
        
        #create security web_sever_sg rule to open port 80
        web_server_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="allow HTTP traffic from port 80"
        )
        
        #create a web server's security group that opens port 80 from anywhere
        RDS_sg = ec2.SecurityGroup(
            self, "RDSSG",
            vpc=network_stack_vpc,
            description="allow HTTP traffic",
            allow_all_outbound=True #TODO: find out if this is what the default should be in our assignment
        )
        
        #create security web_sever_sg rule to open port 3306
        RDS_sg.add_ingress_rule(
            peer=web_server_sg,
            connection=ec2.Port.tcp(3306),
            description="allow HTTP traffic from port 3306"
        )
        
        #Launch one web server in each of the public subnets
        cdk_web_server = ec2.Instance(
            self, "cdk_web_server",
            vpc= network_stack_vpc, # TODO: need to check on if this will work or not
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            security_group=web_server_sg
        )
        
        #RDS instance with MySQL engine with all private subnets as its subnet group
                # Create the RDS instance
        rds_instance = rds.DatabaseInstance(
            self, "MyRdsInstance",
            engine=rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.VER_5_7),
            vpc=network_stack_vpc,
            security_groups=[RDS_sg],
            credentials=rds.Credentials.from_generated_secret("admin"),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO
            ),
            multi_az=True,
            allocated_storage=20,
            vpc_subnets={"subnet_type": ec2.SubnetType.PRIVATE_WITH_EGRESS},
            publicly_accessible=True,
            removal_policy=cdk.RemovalPolicy.DESTROY
        )



        
        

        
