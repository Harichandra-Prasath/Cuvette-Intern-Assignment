## Simple User Management System

### Set-Up

Clone the repository and Enter into the directory  

Create an virtual environment  
```bash
python -m venv .venv
```
   
Activate the virtual environment  
```bash
. .venv/bin/activate
```

If you want to prefer global installations, you can ignore the above  

Install the dependencies  
```bash
pip install -r requirements.txt
```

Apply migrations and migrate to the database  
```bash 
python manage.py makemigrations  
python manage.py migrate  
```

Run the server
```bash
python manage.py runserver
```

**Now the server is up and serving on port 8000**

### Usage

#### Routes 

*All routes are extended from the root(/) path*
  
**/accounts/register/ - Register Route  for New user**  
**/accounts/login/    - Login Route for Registered User**    
**/accounts/logout/   - Logout Route for current Logged User**   
**/users/profile/     - Profile Route for current Logged User**  
**/users/dashboard/   - Welcome Route for  Registered User**    

**Debug is set to True, So you can see all available routes in / route**

#### Guide

Hit Register Route and Fill up the form  
Dont worry about specifics, Form validation is there to handle User Errors  
   
Login with your credentials on login route  
You can use either use registered email or username  
If successfull, You will be redirected to the Welcome page 

Hit up the Profile route to See your Profile  
Make sure you were logged in  

If you want to logout , hit up the logout route  
You will be logged out and redirected to the login page  


#### Notes

Created a Custom User inheriting django's AbstractUser and Altered Email field  
Used login_required decorator for required routes 
Made html templates by django's way of Passing context  
Created Register,Login forms instead of hard-coding the fiedls on Frontend  
