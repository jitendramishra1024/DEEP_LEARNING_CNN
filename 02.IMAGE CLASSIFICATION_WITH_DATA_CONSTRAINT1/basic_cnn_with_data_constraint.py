# -*- coding: utf-8 -*-
"""BASIC_CNN_WITH_DATA_CONSTRAINT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sNZ6QhSk1Is68M4rOWF2aBXFB8FiRvlJ
"""

#################################
#BASIC CNN WITH DATA CONSTRAINT 
#################################
#EARLIER CASE WE USED 
                     #TRAINING SET (8000 IMAGE ) 4000 CAT 4000 DOG IMAGE 
                     #TEST SET     (2000 IMAGE) 1000 CAT  1000 DOG IMAGE 
#IN THIS APPROACH WE WILL USE 
                    #TRAINING SET (3000 IMAGE ) 1500 CAT 1500 DOG IMAGE 
                    #TEST SET     (1000 IMAGE) 500 CAT  500 DOG IMAGE

#3 APPROACHES WE WILL FOLLOW 
                  # 1.BASIC CNN
                  # 2.CNN with regularization
                  # 3.CNN with data generator i.e data augmentation

#####################################################################
#FIRST APPROACH 
 # 1.BASIC CNN
 #TRAINING ACCURACY 0.99
 #VALIDATION ACCURACY 0.75 
 #CONCLUSION OVERFITTED 
#####################################################################

#Mount Google drive
from google.colab import drive 
drive.mount('/content/drive')

from zipfile import ZipFile
file_name = "/content/drive/My Drive/Colab Notebooks/dataset_cat_dog.zip"
with ZipFile(file_name,'r') as zip:
  zip.extractall()
  print("unzipping completed")

# Commented out IPython magic to ensure Python compatibility.
import glob
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, array_to_img

# %matplotlib inline

IMG_DIM = (150, 150)
#As we want         #TRAINING SET (3000 IMAGE ) 1500 CAT 1500 DOG IMAGE 
                    #TEST SET     (1000 IMAGE) 500 CAT  500 DOG IMAGE

cat_train_files = glob.glob('/content/dataset/training_set/cats/*')
dog_train_files = glob.glob('/content/dataset/training_set/dogs/*')
train_files=cat_train_files[:1500]+dog_train_files[:1500]
train_imgs = [img_to_array(load_img(img, target_size=IMG_DIM)) for img in train_files]
train_imgs = np.array(train_imgs)
train_labels = [fn.split('/')[-1].split('.')[0].strip() for fn in train_files]

cat_validation_files = glob.glob('/content/dataset/test_set/cats/*')
dog_validation_files = glob.glob('/content/dataset/test_set/dogs/*')
validation_files=cat_validation_files[:500]+dog_validation_files[:500]
validation_imgs = [img_to_array(load_img(img, target_size=IMG_DIM)) for img in validation_files]
validation_imgs = np.array(validation_imgs)
validation_labels = [fn.split('/')[-1].split('.')[0].strip() for fn in validation_files]

print('Train dataset shape:', train_imgs.shape, 
      '\tValidation dataset shape:', validation_imgs.shape)

#SCALE THE IMAGE AFTER CONVERTING INTO FLLOAT
train_imgs_scaled = train_imgs.astype('float32')
validation_imgs_scaled  = validation_imgs.astype('float32')
train_imgs_scaled /= 255
validation_imgs_scaled /= 255

#ENCODE LABEL :
# encode text category labels
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(train_labels)
train_labels_enc = le.transform(train_labels)
validation_labels_enc = le.transform(validation_labels)

#CREATE A MODEL
input_shape = (150, 150, 3)
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.models import Sequential
from keras import optimizers

model = Sequential()

model.add(Conv2D(16, kernel_size=(3, 3), activation='relu', 
                 input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(),
              metrics=['accuracy'])
print(model.summary())

batch_size = 30
num_classes = 2
epochs = 30
#The batch_size indicates the total number of images passed to the model per iteration.
history = model.fit(x=train_imgs_scaled, y=train_labels_enc,
                    validation_data=(validation_imgs_scaled, validation_labels_enc),
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1)

import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc)+1)

plt.plot(epochs, acc, 'g', label='Training accuracy')
plt.plot(epochs, val_acc, 'r', label='Validation accuracy')
plt.title('Train Accuracy: %.3f, Val Accuracy: %.3f' % (acc[-1], val_acc[-1]), fontsize=12)
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'g', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Train Loss: %.3f, Val Loss: %.3f' % (loss[-1], val_loss[-1]), fontsize=12)
plt.legend()

plt.show()

#####################################################################
#SECOND  APPROACH 
 # 1.BASIC CNN WITH DROP OUT LAYER i.e REGULARIZATION
 #TRAINING ACCURACY 0.95
 #VALIDATION ACCURACY 0.75 
 #CONCLUSION  STILL OVERFITTED 
#####################################################################

model = Sequential()

model.add(Conv2D(16, kernel_size=(3, 3), activation='relu', 
                 input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(),
              metrics=['accuracy'])

model.summary()

batch_size = 30
num_classes = 2
epochs = 30
#The batch_size indicates the total number of images passed to the model per iteration.
history = model.fit(x=train_imgs_scaled, y=train_labels_enc,
                    validation_data=(validation_imgs_scaled, validation_labels_enc),
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1)

import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc)+1)

plt.plot(epochs, acc, 'g', label='Training accuracy')
plt.plot(epochs, val_acc, 'r', label='Validation accuracy')
plt.title('Train Accuracy: %.3f, Val Accuracy: %.3f' % (acc[-1], val_acc[-1]), fontsize=12)
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'g', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Train Loss: %.3f, Val Loss: %.3f' % (loss[-1], val_loss[-1]), fontsize=12)
plt.legend()

plt.show()

#####################################################################
#THIRD  APPROACH 
 # 1.BASIC CNN WITH DATA AUGMENTATION AND REGULARIZATION 
 #TRAINING ACCURACY 0.82
 #VALIDATION ACCURACY 0.73 
 #CONCLUSION   ACCURACY LOW BUT MODEL NOT OVERFITETD  
#####################################################################

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255, zoom_range=0.3, rotation_range=50,
                                   width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, 
                                   horizontal_flip=True, fill_mode='nearest')

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow(train_imgs, train_labels_enc, batch_size=30)
val_generator = val_datagen.flow(validation_imgs, validation_labels_enc, batch_size=20)
#The train_generator generates 30 images each time, so we will use the steps_per_epoch = 100 to train the model on 3,000 randomly generated images from the training data for each epoch.
#The train_generator generates 20 images each time, so we will use the steps_per_epoch = 50 to train the model on 1,000 randomly generated images from the training data for each epoch.

from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.models import Sequential
from keras import optimizers

model = Sequential()

model.add(Conv2D(16, kernel_size=(3, 3), activation='relu', 
                 input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['accuracy'])

model.summary()

history = model.fit_generator(train_generator, steps_per_epoch=100, epochs=100,
                              validation_data=val_generator, validation_steps=50, verbose=1)

import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc)+1)

plt.plot(epochs, acc, 'g', label='Training accuracy')
plt.plot(epochs, val_acc, 'r', label='Validation accuracy')
plt.title('Train Accuracy: %.3f, Val Accuracy: %.3f' % (acc[-1], val_acc[-1]), fontsize=12)
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'g', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Train Loss: %.3f, Val Loss: %.3f' % (loss[-1], val_loss[-1]), fontsize=12)
plt.legend()

plt.show()
