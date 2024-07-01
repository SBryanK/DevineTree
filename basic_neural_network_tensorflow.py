# -*- coding: utf-8 -*-
"""Basic Neural Network Tensorflow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KQpnzuQiEvdQULQcRMd_hkfHgO3dQDd-
"""

import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)

model.evaluate(x_test, y_test)
