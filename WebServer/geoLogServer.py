import json, time
from flask import Flask, request
from flask.ext import restful
import datetime
from numpy import mean


class DataStorage(object):
    
    def __init__(self, file_name):
        self.file = file_name
    def append(self, dict):
        with open(self.file, 'a') as f:
            json.dump(dict, f)

    def get_data(self):
        try:
            with open(self.file) as f:
                json_array = ['{'+x+'}' for x in f.read().strip('{}').split('}{')]
                return [json.loads(x) for x in json_array]
        except:
            return []      


app = Flask(__name__)
api = restful.Api(app)
alldata = DataStorage('data.json')

@app.route('/geoblog')
def hello():
    
    site = '<!DOCTYPE html>' \
         + '<html class="full" lang="en">'\
         + '<head>'\
         + '<meta charset="utf-8">'\
         + '<title>GeoBlog</title>'\
         + '<link href="http://bootswatch.com/cosmo/bootstrap.min.css" rel="stylesheet">'\
         + '</head>'\
         + '<body>'\
         + '<div class="container"> <div class="jumbotron">'\
         + '<h1>GeoBlog</h1>' \
         + '<h3>Average Temperature: ' + str(mean([int(t['temp']) for t in alldata.get_data()])) + '</h3>' \
         + '</div></div><div class="container">'
    for d in alldata.get_data():
        site += '<div class="panel panel-default">'\
              + '<div class="panel-heading"> Received at: ' + d['received'] + '</div>' \
              + '<div class="panel-body">'\
              + '<div> Logging time: ' + d['date'] + '</div>' \
              + '<div> Sensor Id: ' + d['sensorId'] + '</div>' \
              + '<div> Temperature: ' + d['temp'] + '</div></div></div>'

    site += '</div>'\
          + '</body>' \
          + '</html>' 
    return site
          #+ '<script src="js/jquery-1.10.2.js"></script>' \
          #+ '<script src="js/bootstrap.js"></script>' \


class ApiGeoLog(restful.Resource):
    def get(self):	
	   return alldata.get_data()   

    def post(self):
        dataRecieved = request.data
        #print str(dataRecieved)
        data = json.loads(dataRecieved)
        for d in data:
            #print str(d)
            if d['date'] != None and d['temp'] != None and d['sensorId'] != None:
                d['received'] = datetime.datetime.now().strftime("%d. %B %Y %H:%M")
                alldata.append(d)
        
        return 'ok', 200
        
        # else:
        #    return 'Bad Request', 400


api.add_resource(ApiGeoLog, '/geolog')


if __name__ == '__main__':
	#app.debug = True    
	
	app.run(host='0.0.0.0', threaded=True)
