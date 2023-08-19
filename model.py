import ktrain

predictor = ktrain.load_predictor('distilbert')

def get_predictions(x):
    sent = predictor.predict([x])
    return sent[0]