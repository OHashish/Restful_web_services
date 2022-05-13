from flask import Flask
from flask_restful import Api,Resource
import os
import googleapiclient.discovery

app =  Flask(__name__)
api = Api(app)

class GetTrailer(Resource):
    def get(self,name):
            #Authentication
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

            api_service_name = "youtube"
            api_version = "v3"
            DEVELOPER_KEY = "AIzaSyBBV8kjygI42t6q23qMspYeqkdr9SPX8NE"

            youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

            #get 3 results with an input 'name'
            request = youtube.search().list(
            part="snippet",
            maxResults=3,
            q=name
            )
            response = request.execute()      
            
            return response

api.add_resource(GetTrailer,"/Trailer/<string:name>")
if __name__=='__main__':
    #app.run(debug=True)
    app.run(host='127.0.0.1', port=5001)
    