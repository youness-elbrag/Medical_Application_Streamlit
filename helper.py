from keras.models import load_model
from keras.preprocessing import image
import cv2
import numpy as np
import base64
import streamlit as st


@st.cache(allow_output_mutation=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)  
     
def get_img_array(img_path, size):
    # `img` is a PIL image of size 64x64
    #img =image.load_img(img_path, target_size=(size,size,3))
    src = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    resized=cv2.resize(src,(size,size))
    # `array` is a float32 Numpy array of shape (64,64, 3)
    img =image.img_to_array(resized)
    # We add a dimension to transform our array into a "batch"
    # of size (1, 64, 64, 3)
    img = img/255
    #img=img.reshape(1,size,size,3)
    return img

def load_cnn_model(model_path):
    model = load_model(model_path)
    return model


Sitution_Medical={'Normal':' you are healthy no probelm adressed in your sitution',
                  'Stey' :'consider this sitution \n  you have ,A person with a stye will have a painful red swelling on the eyelid,\n making the eye produce tears and become red. Often the lump looks like a boil  ',
                  'jaundice':'The whites of your eyes (called the sclera) turn yellow when you have a condition called jaundice. \nThe whites of your eyes might turn yellow when your body has too much of \n a chemical called bilirubin, a yellow substance that forms when red blood cells break down',
                  'uveitis':'Uveitis can cause problems like pain, redness, and vision loss. \n Uveitis damages the part of the eye called the uvea — but it often affects other parts of the eye,\n too. Sometimes uveitis goes away quickly, but it can come back.',
                  'Pink':'Pink eye (conjunctivitis) is the inflammation or infection of the transparent membrane that lines your eyelid and eyeball '
}    

classes= ['jaundice','normal','pink','stye','uveitis']
def make_prediction(output,proba):    
    for j in range(1):
        if classes[output[j]] == classes[0]:
            st.write("{}".format(classes[output[j]])+" ({:.3%})".format(proba[0][output[j]]),unsafe_allow_html=True)
            st.write(Sitution_Medical.get('jaundice'),unsafe_allow_html=True)
        elif classes[output[j]]== classes[2]:
            st.write("{}".format(classes[output[j]])+" ({:.3%})".format(proba[0][output[j]]),unsafe_allow_html=True)
            st.write(Sitution_Medical.get('Pink'),unsafe_allow_html=True)
        elif classes[output[j]]== classes[3]:
            st.write("{}".format(classes[output[j]])+" ({:.3%})".format(proba[0][output[j]]),unsafe_allow_html=True)
            st.write(Sitution_Medical.get('Stey'),unsafe_allow_html=True)  
        elif classes[output[j]] == classes[4]:
            st.write("{}".format(classes[output[j]])+" ({:.3%})".format(proba[0][output[j]]),unsafe_allow_html=True)
            st.write(Sitution_Medical.get('uveitis'),unsafe_allow_html=True) 
        else:
            st.write(Sitution_Medical.get('Normal'),unsafe_allow_html=True)
        
		   #st.text(f"The predicted result is {resutlts}")