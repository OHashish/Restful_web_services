Description
Webservice 1: when a famous movie quote is entered ,it gets all famous movie quotes from movie directed by the directory of the famouse movie.
Webservice 2: gets all movies directed by a specified director (small local .csv)
Webservice 3: uses YouTube API to get movie trailers 


Web Service 1
-use java 1.8
-dependencies jersey jar files 
-use intelliJ to run the FirstRESTStartup.java file to run the server.
Web Service 2
-use java 1.8
-dependencies jersey jar files 
-use intelliJ to run the ServiceTwoStartUp.java file to run the server.
Web Service 3
-It is located in file main.py
-The external service uses python and the requirmenets are in requirements.txt
-For the api you need to use pip for the following:
pip install --upgrade google-api-python-client
pip install --upgrade google-auth-oauthlib google-auth-httplib2

Integrated Client
-It is located in IntegClient.py
The integrated Client runs on python (Flask)
-for the you need to:
pip install flask

To run the web application server:
You need to run web service 1 and web service 2 in intellij at the same time
then you need to run webservice 3 which is main.py
then run IntegClient.py and open the relevent port (http://127.0.0.1:5000/) in browser
