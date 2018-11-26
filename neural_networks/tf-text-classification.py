#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf
from tensorflow import keras

import numpy as np


# get the IMBD reviews data
imdb = keras.datasets.imdb

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=10000)


# A dictionary mapping words to an integer index
word_index = imdb.get_word_index()

# The first indices are reserved
word_index = {k:(v+3) for k,v in word_index.items()} 
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text])


X_train = keras.preprocessing.sequence.pad_sequences(X_train,
                                                     value=word_index["<PAD>"],
                                                     padding='post',
                                                     maxlen=256)

X_test = keras.preprocessing.sequence.pad_sequences(X_test,
                                                    value=word_index["<PAD>"],
                                                    padding='post',
                                                    maxlen=256)



# input shape is the vocabulary count used for the movie reviews (10,000 words)
vocab_size = 10000

model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation=tf.nn.relu))
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

model.summary()


model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='binary_crossentropy',
              metrics=['accuracy'])


x_val = X_train[:10000]
partial_x_train = X_train[10000:] # 15k records

y_val = y_train[:10000]
partial_y_train = y_train[10000:] # 15k records


history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=40,
                    batch_size=512,
                    validation_data=(x_val, y_val),
                    verbose=1)


results = model.evaluate(X_test, y_test)

print(results)


hist_dict = history.history
hist_dict.keys()


import matplotlib.pyplot as plt

get_ipython().magic(u'matplotlib inline')

acc = hist_dict['acc']
val_acc = hist_dict['val_acc']
loss = hist_dict['loss']
val_loss = hist_dict['val_loss']

epochs = range(1, len(acc) + 1)

# "bo" is for "blue dot"
plt.plot(epochs, loss, 'bo', label='Training loss')
# b is for "solid blue line"
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()


plt.clf()   # clear figure
acc_values = hist_dict['acc']
val_acc_values = hist_dict['val_acc']

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()
