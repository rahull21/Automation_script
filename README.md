# Automation_script
This is an automation script that provides a given user with  appearing display name access to a given repository on a workspace in which the user is a member.

The admin has to create an app password and authenticate call to BitBucket via admin username and App_password Authentication . 

The admin username should be updated in the username variable and the App password should be updated in the app_password variable.

the user who wants access, his display name should be updated in the display_name and repository name 
should be put in the repo_slug column, similarly, workspace name should be entered in the workspace-slug variable.

Dependencies required : a) Json
                        b) Requests