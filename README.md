# Backend Assignment
## How to run
---
There are two different applications that run independently named api and web in the repository.<br>
<br>
To run api,<br>
1. Create a spotify app from spotify developers dashboard and get app's client id and client secret.
2. Open a terminal session and navigate to the src/api folder.
3. In this folder run following commands,

        export FLASK_APP=app.py;
        export FLASK_RUN_PORT=5050;
        export SPOTIPY_CLIENT_ID=<your_apps_client_id>;
        export SPOTIPY_CLIENT_SECRET=<your_apps_client_secret>;
        flask run

<br>
To run web app,<br>

1. Open another terminal session and navigate to src/web folder.
2. In this folder run following commands,

        export FLASK_APP=app.py;
        flask run
<br>
After running both of the applications you can go to localhost:5000/search and search for top tracks of a random artist of given genre.