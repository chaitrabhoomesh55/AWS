#Create 2 users from aws cli and 2 groups from aws cli-Dev & QA; u need to attach 1 user to Dev and 1 user to QA using aws cli 
#same thing i need to do using python script also;
import boto3

boto3.setup_default_session(profile_name='admin')           

iam = boto3.client('iam')
group_names = ['DEV','QA', 'DEV2']
user_names = ['user1', 'user2', 'Chia', 'Chicken']

response = iam.list_groups()
print("Response:",response)
groups =[]
for group in response['Groups']:
    print(group['GroupName'])
    groups.append(group['GroupName'])
print("GROUPS:",groups)


# Create the IAM group
for groupname in group_names:
    if groupname not in groups:
        iam.create_group(GroupName=groupname)
        print(f'the {groupname} group got created')
    else:
        print(f'the {groupname} group already exists')

response = iam.list_users()
print("response:", response)

users = []
for user in response['Users']:
    #if user['UserName']:
    users.append(user['UserName'])
print(users)

for user in user_names:
    if user not in users:
        iam.create_user(UserName=user)
        print(f'the user {user} just got created')
    else:
        print(f'the user {user} exists already')
        
#for user in users: 
    #if user in group_names:
        #print(f'user {user} exist in {group}')



'''
#check if user[] is present for each group[]
#create github and repo and push 
#add a file called .gitignore, insite that add aws_setup.txt

{
    'Groups': [
        {
            'Path': 'string',
            'GroupName': 'DEV',
            'GroupId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1)
        },
        {
            'Path': 'string',
            'GroupName': 'QA',
            'GroupId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1)
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}

response: {'Users': [{'Path': '/', 'UserName': 'Chia', 'UserId': 'AIDA5JV4IEHIRSQGR4UNY', 
'Arn': 'arn:aws:iam::914149089745:user/Chia', 'CreateDate': datetime.datetime(2023, 10, 10, 18, 10, 45, tzinfo=tzutc()), 
'PasswordLastUsed': datetime.datetime(2023, 10, 10, 18, 11, 49, tzinfo=tzutc())}], 'IsTruncated': False, 
'ResponseMetadata': {'RequestId': '912a470e-6ee7-4d8a-8537-e22411de77a9', 'HTTPStatusCode': 200, 
'HTTPHeaders': {'x-amzn-requestid': '912a470e-6ee7-4d8a-8537-e22411de77a9', 'content-type': 'text/xml', 
'content-length': '611', 'date': 'Wed, 11 Oct 2023 19:25:54 GMT'}, 'RetryAttempts': 0}}

iam = boto3.resource('iam')
print("IAM",iam)


#GROUPS:
group1 = iam.Group('DEV')
print("GROUP:",group1)


role = iam.Role('DEV')
print("ROLE:",role)


group2 = iam.Group('QA')
print("GROUP:",group2)

role = iam.Role('QA')
print("ROLE:",role)


git init
add index.html
git commit -m "Add index.html"

git remote add origin https://github.com/chaitrabhoomesh55/AWS.git
#Before creating a new branch, pull the changes from upstream. Your master needs to be up to date::  $ git pull
#Create the branch on your local machine and switch in this branch : $ git checkout -b [name_of_your_new_branch]
#Push the branch on github : $ git push origin [name_of_your_new_branch]
#git branch -M 'main'    #git checkout -b <new_branch_name>
git push -u origin 'main'

git add .
git commit -m "Commit message"
git push origin main
'''