import requests
import json


username = ''
app_password = ''

workspace_slug = ''
repo_slug = ''
display_name = ''


url = f"https://api.bitbucket.org/2.0/workspaces/{workspace_slug}/permissions"

headers = {
    "Content-Type": "application/json"
}

response = requests.get(
    url,
    headers=headers,
    auth=(username, app_password)
)

members = json.loads(response.text)['values']
#print(members)

user_uuid = None
for member in members:
    if member['type'] == 'workspace_membership' and member['user']['display_name'] == display_name:
        user_uuid = member['user']['uuid']
        
        break

if not user_uuid:
    print(f"Could not find user with display name '{display_name}'")
else:
    url = "https://api.bitbucket.org/2.0/repositories/{workspace_slug}/{repo_slug}/permissions-config/users/{}"
url = url.format(user_uuid)

username = ""
app_password = ""


permission = "write"


data = {
    "permission": permission
}


headers = {
    "Content-Type": "application/json"
}


auth = (username, app_password)

response = requests.put(url, headers=headers, data=json.dumps(data), auth=auth)
print(response)

if response.status_code == 200:
    print("User permission updated successfully!")
else:
    print("Error updating user permission: " + response.text)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
   # url = "https://api.bitbucket.org/2.0/repositories/{workspace_slug}/{repository_slug}/permissions-config/users/"

    #payload = {
      #  "user": {
      #      "uuid": user_uuid
     #   },
     #   "permission": "write"
    #}

    #response = requests.post(
     #   url,
     #   headers=headers,
      #  auth=(username, app_password),
     #   json=payload
    #)
    #print(response)

if response.status_code == 200:
        print(f"Successfully added user '{display_name}' to repository '{repo_slug}'")
else:
        print(f"Failed to add user '{display_name}' to repository '{repo_slug}': {response.text}")
