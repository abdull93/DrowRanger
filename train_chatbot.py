import nltk
import json
import pickle
import numpy as np
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.metrics import categorical_crossentropy
from keras.utils.vis_utils import plot_model
from keras.optimizers import Adam
import random
import os
import msvcrt


data_file = open('intents.json').read()
intents = json.loads(data_file)

words=[]
classes = []
documents = []
ignore_words = ['?', '!']
#bndefo 
for intent in intents['intents']:
    for pattern in intent['patterns']:

       
        w = nltk.word_tokenize(pattern)
        words.extend(w)
       
        documents.append((w, intent['tag']))

        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))
print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique lemmatized words", words)


pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))


training = []

output_empty = [0] * len(classes)

for doc in documents:
    
    bag = []
   
    pattern_words = doc[0]
    
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
   
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    
    training.append([bag, output_row])
random.shuffle(training)
training = np.array(training)

x1 = list(training[:,0])
y2 = list(training[:,1])
x = np.array(x1)
y = np.array(y2)

print("Training data created")
model = Sequential([
    Dense(128, input_shape=(len(x[0]),)),
    Activation('relu'),
    Dropout(0.25),
    Dense(64),
    Activation('tanh'),
    Dropout(0.15),
    Dense(len(y[0]),),
    Activation('softmax'),    
])

model.summary()

model.compile(Adam(lr=0.002) ,loss='categorical_crossentropy', metrics=['accuracy'])
hist = model.fit(x,y ,validation_split=0.1, epochs=200, batch_size=5, verbose=1)
plt.plot(hist.history['accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()
plt.plot(hist.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()


print("Data Trained ")
model.save('Model.h5', hist)
print("Press any key to exit")
msvcrt.getch()
