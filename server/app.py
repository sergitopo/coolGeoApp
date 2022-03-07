from flask import Flask
from flask import jsonify
from flask import request
import turnover_repository

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the rest api designed by Sergi Soler'


@app.route('/turnover/stats/sum', methods=['GET'])
def accumulated(geometry, startdate, enddate):
    """
    Serves data for wireframe's widget at position 1. 
    It accepts query params for geometry and date filters. Geometry is described as WKT and dates in yyyy-MM-dd format
    It returns a single number as the total turnover between dates and postal codes within the geometry (map viewport)
    """
    pass


@app.route('/turnover/stats/timeseries', methods=['GET'])
def timeSeries(geometry, startdate, enddate):
    """
    Serves data for wireframe's widget at position 2. 
    It accepts query params for geometry and date filters. Geometry is described as WKT and dates in yyyy-MM-dd format
    It returns monthly aggregated turnover for each gender ordered by date ascending
    """
    pass


@app.route('/turnover/stats/byage>', methods=['GET'])
def get_turnover_by_age(geometry, startdate, enddate):
    """
    Serves data for wireframe's widget at position 3. 
    It accepts query params for geometry and date filters. Geometry is described as WKT and dates in yyyy-MM-dd format
    It returns the turnover grouped by age group and gender ordered by age gruop ascending
    """
    pass


@app.route('/turnover/postalcode/<int:code>', methods=['GET'])
def getInfo(code) -> dict :
    """
    Serves data for wireframe's map postal codes turnover layer on postal code click event. 
    It requires the postal code
    It returns the turnover info for that postal code aggregated by age group and gender
    """
    return turnover_repository.getTurnoverInfoByPostalCodeId(code)


@app.route('/layers/postalcodes', methods=['GET'])
def postalCodes() -> str:
    """
    Serves data for wireframe's map postal codes turnover layer. 
    It accepts query params for geometry and date filters. Geometry is described as WKT and dates in yyyy-MM-dd format
    It returns the geometry, postal code and aggregated turnover for each postal code
    """    
    return jsonify(turnover_repository.getBoundaryPostalCodesStats(request.args.get("geometry"), request.args.get("startdate"), request.args.get("enddate")))


@app.route('/layers/union', methods=['GET'])
def region():
    pass



app.run(host='0.0.0.0', port=9999, debug=True)