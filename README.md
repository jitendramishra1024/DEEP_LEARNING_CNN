# DEEP_LEARNING_CNN
This repository contains code for  CNN projects for Image classification 





***************************************

01.CAT_DOG_CLASSIFIER 

***************************************
APPLIED TECHNIQUE :
CNN :Conv2D(32,(3,3))->Conv2D(64,(3,3))->->Conv2D(128,(3,3))->DENSE(256)->DENSE(256)->DENSE(1) -Sigmoid

Maxpooling after every conv2D layer , done batch normalization and data augmentation 

ACCURACY ACHIEVED (TRAINING :82% , TESTING ACCURACY :79% ) in 30 EPOCHS

***************************************

We are going  to test an provided image is dog or cat
Dataset :https://drive.google.com/drive/folders/1YG-TbCe0r6RY3hbl2I4zKC5eZIPCXEFF?usp=sharing


i.e binary classification using Convolution neural network

dataset description  :

training_set: 4000 cat image 4000 dog image 

test_set: 1000 cat image 1000 dog image 

single_prediction :2 images cat_or_dog 

STEPS :

    1.upload dataset.zip to google drive Colab Notebooks 

    2.Upload code 

    3. run CAT_DOG_CLASSIFIER.ipynb 

Features :
Added drop out layer , added data augmentation to reduce overfitting
Final model saved into h5 file and model prediction done from h5 file 
plotted graph to show training and test accuracy over epochs 

02. CNN WITH DATA CONSTRAINTS 


