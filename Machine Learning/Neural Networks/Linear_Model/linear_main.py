import tensorflow as tf
from tensorflow import keras

import pandas as pd
import numpy as np

train_df = pd.read_csv('./data/train.csv')
np.random.shuffle(train_df.values)

# Convert dataframe to numpy array
print('           Data                ')
print('---------------------------')
print(train_df.head())
print('---------------------------')

model = keras.Sequential([
    # Hidden layer with 4 nodes
    keras.layers.Dense(4, input_shape=(2, ), activation="relu"),
    # Output layer with 2 nodes (Output point can be red or blue)
    keras.layers.Dense(2, activation="sigmoid")])

# Compile model
model.compile(optimizer="adam",
              loss=keras.losses.SparseCategoricalCrossentropy(
                  from_logits=True),
              metrics=['accuracy'])

# fit model
x_train = np.column_stack((train_df.x.values, train_df.y.values))
y_train = train_df.color.values
model.fit(x_train, y_train, batch_size=4, epochs=5)

test_df = pd.read_csv('./data/test.csv')
test_x = np.column_stack((test_df.x.values, test_df.y.values))
print('----Evaluation ---')
model.evaluate(test_x, test_df.color.values)
