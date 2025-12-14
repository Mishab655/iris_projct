from flask import Flask, request, jsonify
from app.predict import predict_species

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data["features"]
    result = predict_species(features)
    return jsonify({"prediction": result})


if __name__ == "__main__":
    app.run(debug=True)
