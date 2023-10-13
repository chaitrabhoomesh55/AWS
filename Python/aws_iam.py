import boto3


boto3.setup_default_session(profile_name='admin')

# Create a Boto3 IAM client
iam_client = boto3.client('iam')

# Use the list_users() method to retrieve a list of IAM users
response = iam_client.list_users()
print(type(response))

role = iam.create_role(
    Path='string',
    RoleName='QA',
    AssumeRolePolicyDocument='string',
    Description='string',
    MaxSessionDuration=123,
    PermissionsBoundary='string'
)
print("ROLE:", role)


# Print the list of users
for user in response['Users']:
    print(f"User Name: {user['UserName']}")





'''
Create 2 users from aws cli and 2 groups from aws cli-Dev & QA; u need to attach 1 user to Dev and 1 user to QA using aws cli 
same thing i need to do using python script also;

Dev1-
'''
