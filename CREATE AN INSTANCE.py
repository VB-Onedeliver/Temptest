import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId = 'ami-97785bed',
    MinCount = 2,
    MaxCount = 2,
    InstanceType = 't2.micro')
print(instance[0].id)



