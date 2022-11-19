![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Drakain,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!



## Deployment
  * Head to Heroku and click the "New" tab and select "Create new app"
  * Choose a unique app name and click "Create app"
  * Click to the "Settings" tab and then head down to the "Config vars" section
  * Click "Reveal Config Vars" and add a Config Var called "PORT" (key) with a value of "8000" (value)
  * Head down to the "Buildpacks" section and click "Add buildpack"
  * Choose "Python" save the changes
  * Add a second buildpack called "nodejs"
  * Click the "Deploy" tab and go down to the "Deployment method" section
  * Choose "GitHub" and then search for the project in the new section that appears
  * Click the "Connect" button once the project has been found
  * Choose either "Enable Automatic Deploys" in the "Automatic deploys" section or "Deploy Branch" in the "Manual Deploy" section