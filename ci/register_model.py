from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Model
from config_utils import load_config

config = load_config()
ml_client = MLClient(
    DefaultAzureCredential(),
    config['subscription_id'],
    config['resource_group'],
    config['workspace_name']
)

model = Model(
    name='linear_regression_model',
    path='model.joblib',
    description='Linear regression model'
)

ml_client.models.create_or_update(model)
print("Model registered.")
