
## USING THE PITCH APP

+ First clone The Project from github.
+ Then setup the project by creating a virtual environment and installing all the packages by running ``` pip3 install -r requirements.txt ``` 
+ Then on the terminal start the server by running ``` python manage.py runserver ```
+ On any browser type ``` https://localhost:5000```


# BEHAVIOUR

## Authentication

+ Once the url is entered the user is welcomed to the home page where they can be redirected to the registration and login form.  
- If the user has not signed up, he/she can only view the categories and can't vote or comment.
- The user is required to register then log in for them to have certain priviledges on the app.
- The user can also sign out once they are logged in.

## Pitches.

+ The user can add pitches and they get displayed from the most resent one.
+ The user can upvote,downvote and comment on a pitch.
+ The pitch information is displayed alongside other pitches, a pitch contains information such as pitch body, pitch author, downvotes and upvotes.


## Categories

+ The user can view all these categories whether authenticated or not.
+ The pitches are categorized according to what the user decides to add as a pitch category