import mlflow
from sklearn.ensemble import RandomForestClassifier

def train():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

if accuracy < 0.8:
    raise Exception("Model is bad")
