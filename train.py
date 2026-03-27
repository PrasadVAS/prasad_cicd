import mlflow
from sklearn.ensemble import RandomForestClassifier

def train():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model
