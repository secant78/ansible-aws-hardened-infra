#!/usr/bin/env python3
import json
import boto3

def get_inventory():
    ec2 = boto3.client('ec2', region_name='us-east-2')
    response = ec2.describe_instances(
        Filters=[{'Name': 'tag:Role', 'Values': ['webserver', 'database']}]
    )
    
    inventory = {'_meta': {'hostvars': {}}}
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            role = next(t['Value'] for t in instance['Tags'] if t['Key'] == 'Role')
            ip = instance.get('PublicIpAddress') or instance.get('PrivateIpAddress')
            
            if role not in inventory:
                inventory[role] = {'hosts': []}
            inventory[role]['hosts'].append(ip)
            
    return inventory

if __name__ == "__main__":
    print(json.dumps(get_inventory(), indent=2))	
