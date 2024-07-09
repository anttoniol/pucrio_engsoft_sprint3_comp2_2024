from flask import Flask,jsonify,request
from flask_swagger_ui import get_swaggerui_blueprint
import service

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Event storage API'
    }
)

app = Flask(__name__)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


def build_response(success, result, status):
    return jsonify(
        response = {
            "success": success,
            "result": result
        },
        status=status
    )

@app.route("/healthcheck")
def health_check():
    return jsonify({
        "Message": "The Storage API is running successfully"
    })


@app.route("/<id>", methods=["GET"])
def get_by_id(id):
    try:
        return build_response(True, service.get_by_id(id), 200)
    except Exception as ex:
        error_message = "Error when getting event by ID: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


@app.route("/", methods=["GET"])
def get_by_coordinates():
    lat = request.args.get('latitude')
    lon = request.args.get('longitude')

    try:
        return build_response(True, service.get_by_coordinates(lat, lon), 200)
    except Exception as ex:
        error_message = "Error when getting event by coordinates: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


@app.route("/", methods=["POST"])
def save():
    data = request.get_json()

    try:
        return build_response(True, service.save(data), 200)
    except Exception as ex:
        error_message = "Error when saving event: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


@app.route("/<id>", methods=["DELETE"])
def delete(id):
    try:
        return build_response(True, service.delete(id), 200)
    except Exception as ex:
        error_message = "Error when deleting event: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


@app.route("/<id>", methods=["PUT"])
def update(id):
    data = request.get_json()

    try:
        return build_response(True, service.update(id, data), 200)
    except Exception as ex:
        error_message = "Error when updating event: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
