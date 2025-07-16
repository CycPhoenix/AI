import pandas as pd
from tensorflow.keras.models import load_model

model = load_model('models/mymodel.h5')

# Load validation dataset
df_val = pd.read_csv('data/validation_dataset.csv') # Add validation dataset as needed
X_val = df_val['test']
y_val = df_val['label'] # You may need to encode labels as well

# Preprocess validation data (similar to training data)

# Evaluation the model
loss, accuracy = model.evaluate(X_val, y_val)
print(f"Validation Loss: {loss}, Validatiion Accuracy: {accuracy}")
