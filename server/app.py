from flask import Flask
from turnover_repository import getTurnoverInfoByPostalCodeId

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the rest api designed by Sergi Soler'


@app.route('/turnover/stats/sum', methods=['GET'])
def accumulated(geometry: str):
    pass

######## Endpoint

@app.route('/turnover/stats/timeseries', methods=['GET'])
def timeSeries(geometry: str):
   pass

######## Endpoint

@app.route('/turnover/stats/byage', methods=['GET'])
def get_turnover_by_age(geometry: str):
   pass

######## Endpoint

@app.route('/turnover/postalcode/<int:code>', methods=['GET'])
def getInfo(code) -> dict :
    return getTurnoverInfoByPostalCodeId(code)

######## Endpoint

@app.route('/layers/postalcodes', methods=['GET'])
def postalCodes():
    pass


######## Endpoint

@app.route('/layers/region', methods=['GET'])
def region():
    pass



app.run(port=9999, debug=True)