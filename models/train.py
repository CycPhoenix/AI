import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from model import create_model

# Load dataset
df = pd.read_csv('data/dataset.csv')
x = df['test'] # Features
y = df['label'] # Labels

# Preprocessing (example: encoding labels)
y_encoded = pd.get_dummies(y).values # One-hot encoding
X_train, X_val, y_train, y_val = train_test_split(X, y_encoded, test_size=0.2)

# Convert text data to numerical format (e.g., using Tokenizer, embeddings, etc.)
# Placeholder for preprocessing (e.g, using a tokenizer)

model = create_model()
model.fit(X_train, y_train, validation_date-(X_val, y_val), epochs=10)
model.save('models/my_model.h5') # Save the trained model
