from app.model import train_model


def predict_species(features):
    model = train_model()
    prediction = model.predict([features])
    return int(prediction[0])
