# DEEP_LEARNING_CNN
This repository contains code for  CNN projects for Image classification  <br/>

##01.CAT_DOG_CLASSIFIER 
###APPLIED TECHNIQUE :
CNN :Conv2D(32,(3,3))->Conv2D(64,(3,3))->->Conv2D(128,(3,3))->DENSE(256)->DENSE(256)->DENSE(1) -Sigmoid<br/>
Maxpooling after every conv2D layer , done batch normalization and data augmentation <br/>
ACCURACY ACHIEVED (TRAINING :82% , TESTING ACCURACY :79% ) in 30 EPOCHS<br/>

***************************************

We are going  to test an provided image is dog or cat
Dataset :https://drive.google.com/drive/folders/1YG-TbCe0r6RY3hbl2I4zKC5eZIPCXEFF?usp=sharing


i.e binary classification using Convolution neural network

dataset description  :

training_set: 4000 cat image 4000 dog image <br/>
test_set: 1000 cat image 1000 dog image <br/>
single_prediction :2 images cat_or_dog <br/>

STEPS :

    1.upload dataset.zip to google drive Colab Notebooks 

    2.Upload code 

    3. run CAT_DOG_CLASSIFIER.ipynb 

Features :
Added drop out layer , added data augmentation to reduce overfitting
Final model saved into h5 file and model prediction done from h5 file 
plotted graph to show training and test accuracy over epochs 

02. BASIC CNN WITH DATA CONSTRAINTS 

From the above example we experimented with data constraint i.e

TRAINING SET :1500 CAT 1500 DOG 
TEST SET     : 500 CAT 500 DOG 

3 APPROACHES TRIED 

#FIRST APPROACH 
 #.BASIC CNN
 #TRAINING ACCURACY 0.99
 #VALIDATION ACCURACY 0.75 
 #CONCLUSION OVERFITTED 

#SECOND  APPROACH 
 # BASIC CNN WITH DROP OUT LAYER i.e REGULARIZATION
 #TRAINING ACCURACY 0.95
 #VALIDATION ACCURACY 0.75 
 #CONCLUSION  STILL OVERFITTED 
 
#THIRD APPROACH 
 # BASIC CNN WITH DROP OUT LAYER i.e REGULARIZATION WITH DATA AUGMENTATION 
 #TRAINING ACCURACY 0.82
 #VALIDATION ACCURACY 0.73
 #CONCLUSION: ACCURACY LOW BUT MODEL NOT OVERFITTED 

03. CNN WITH TRANSFER LEARNING PRETRAINED AND TRANSFER LEARNING 


From the above example we experimented with data constraint i.e

TRAINING SET :1500 CAT 1500 DOG 
TEST SET     : 500 CAT 500 DOG 

3 APPROACHES TRIED 



#FIRST APPROACH 

 #VGG16 Pre-trained CNN model as a Feature Extractor with out data augmentation 
 #TRAINING ACCURACY :1.00
 #VALIDATION ACCURACY:0.89  
 #CONCLUSION: OVERFITTED 






#SECOND  APPROACH 

 #VGG16 Pre-trained CNN model as a Feature Extractor with data augmentation 
 #TRAINING ACCURACY :0.88
 #VALIDATION ACCURACY:0.99  
 #CONCLUSION: MODEL UNDER FITTED



#THIRD  APPROACH 

 #VGG16 Pre-trained CNN model with Fine-tuning and Image Augmentation
 #TRAINING ACCURACY :0.99
 #VALIDATION ACCURACY:0.95 
 #CONCLUSION: MODEL IS PERFECT
