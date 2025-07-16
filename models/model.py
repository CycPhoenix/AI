import tensorflow as tf
print(tf.__version__)
from tensorflow import keras
print("Keras imported successfully")

def create_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(100,))) # Adjust input_shape based on your dataset
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(3, activation='softmax')) # Adjust number of outputs based on your classes
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model
