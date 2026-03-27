import mlflow

mlflow.register_model(
    "runs:/<run_id>/model",
    "credit_model"
)
