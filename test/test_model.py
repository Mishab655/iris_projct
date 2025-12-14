from app.predict import predict_species


def test_prediction_output_type():
    features = [5.1, 3.5, 1.4, 0.2]
    result = predict_species(features)
    assert isinstance(result, int)
