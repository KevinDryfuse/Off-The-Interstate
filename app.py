# app.py
from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
app = Flask(__name__)


@app.route('/geoinfo/', methods=['GET'])
def getinfo():
    # Retrieve the name from url parameter
    latlng = request.args.get("latlng", None).split(",")
    geolocator = Nominatim(user_agent="off_the_interstate")
    location = geolocator.reverse(request.args.get("latlng", None))

    # For debugging
    print(f"got lat {location.latitude}")
    print(f"got long {location.longitude}")

    response = {}
    response["MESSAGE"] = f"Location {location.address} provided!"

    # Return the response in json format
    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_example():
    value = request.form.get('value')
    print(value)

    if value:
        return jsonify({
            "Message": f"Value {value} submitted!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no value found, please send a value."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Off the Interstate Landing Page</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)