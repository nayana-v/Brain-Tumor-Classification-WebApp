

import streamlit as st 
import tensorflow as tf
#import cv2
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, BatchNormalization, Flatten
import numpy as np
from PIL import Image ,ImageOps


st.set_option('deprecation.showfileUploaderEncoding',False) #on loading a streamlit app we get a warning, this line prevents us from getting that warning

@st.cache(allow_output_mutation=True) #this line prevent us from loading the model again and again and will help in storing the model in cache once it has been loaded


model=tf.keras.models.load_model('BrainTumorModel .h5')
#defining the header or title of the page that the user will be seeing. We also make a side bar for the web app
image1=Image.open('RVlogo.jpg')
st.image(image1,use_column_width=False)
st.markdown("<h1 style='text-align: center; color: Black;'>Brain Tumor Classifier</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Black;'>All you have to do is Upload the MRI scan and the model will do the rest!</h3>", unsafe_allow_html=True)
#st.markdown("<h4 style='text-align: center; color: Black;'>Submission for HackOff V3.0</h4>", unsafe_allow_html=True)
st.sidebar.header("What is this Project about?")
st.sidebar.text("It is a Deep learning solution to detection of Brain Tumor using MRI Scans.")
st.sidebar.header("What does it do?")
st.sidebar.text("The user can upload their MRI scan and the model will try to predict whether or not the user has Brain Tumor or not.")
st.sidebar.header("What tools where used to make this?")
st.sidebar.text("The Model was made using a dataset available in figshare. We made use of Tensorflow, Keras as well as some other Python Libraries to make this complete project. To depoly it on web, we used ngrok and Streamlit!")
st.sidebar.text("Brain tumor classification is a crucial task to evaluate the tumors and make a treatment decision according to their classes. There are many imaging techniques used to detect brain tumors. However, MRI is commonly used due to its superior image quality and the fact of relying on no ionizing radiation. Deep learning (DL) is a subfield of machine learning and recently showed a remarkable performance, especially in classification and segmentation problems.")



file=st.file_uploader("Please upload your MRI Scan",type = ["jpg","png"]) #accepting the image input from the user

def import_and_predict(image_data,model): #our prediction method that will accept the data and the model and would give us a prediction
  #pre-processing the image before it is fed to the model
  #img_array = cv2.imread(image_data,cv2.IMREAD_GRAYSCALE) #loading the images in grayscale
  #new_array = cv2.resize(image_data,(150,150)) 
                 #adding our data in to the training_data list which we will use to define our X and y for train-tets split
  #X = np.array(new_array).reshape(-1,150,150)
    #print(X.shape)
  #X = X/255.0  
  #X = X.reshape(-1,150,150,1)
  #res = model.predict(X) 
  size = (150,150)
  image1 = ImageOps.fit(image_data,size,Image.ANTIALIAS)
  image = ImageOps.grayscale(image1)
  img = np.array(image).reshape(-1,150,150)
  img_reshape = img[np.newaxis,...]
  img_reshape = img_reshape/255.0
  img_reshape = img_reshape.reshape(-1,150,150,1)
  prediction = model.predict(img_reshape)
  #print(np.argmax(prediction))
  return prediction

if file is None: #initial condition when no image has been uploaded by the user
  st.markdown("<h5 style='text-align: center; color: Black;'>Please Upload a File</h5>", unsafe_allow_html=True)
else: #condition to give the result once the user has input the image 
  image = Image.open(file)
  st.image(image,use_column_width = False)
  predictions = import_and_predict(image,model)
  class_names = ['Glioma Tumor','Meningioma_Tumor','No Tumor','Pituitary Tumor']
  string = "The patient is most likely to have: "+ class_names[np.argmax(predictions)]

  #st.success(np.argmax(predictions))
  st.success(string)
#st.markdown("<h7 style='text-align: center; color: Black;'>The project was developed by Hamsa G and Nayana V under the guidance of Dr.Veena Devi, RVCE.</h7>", unsafe_allow_html=True)
  #st.success(predictions)
string2="The project was developed by Hamsa G and Nayana V under the guidance of Dr.Veena Devi, RVCE."
st.success(string2)
