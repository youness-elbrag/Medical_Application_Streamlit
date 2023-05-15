from typing import final
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from helper import *
import time
import os 
import glob
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE

st.set_page_config(
    layout="wide",
    page_title="A-EYE - Detection sitution Medical from eye",
    page_icon="👁",
    )
#st.write(f'<style>{local_css("style.css")}</style>', unsafe_allow_html=True)
components.html(
    """
        <link href="./style.css" rel="stylesheet">
    """
)

set_bg('./img/background.jpg') 

###########################
# 👇      CODE        👇 #
###########################

with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

row1_1, row1_2 = st.columns((2,2))


#####################################
# 👇      Load the modol wieghts         👇 #
#####################################
model_path="./model/Cnn_detector.h5"
IMAGE_SIZE = 32
save_input_img="./predicted_imges"
######################################

with row1_1:
    st.image('./img/eye_logo.png', width=200)
    st.markdown("""
        ##
        """)
    st.markdown("""
        ####

        Upload an eye Facial  !

        Our **Artificial Intelligence Expert system diagnosis** trained with more than **1 326 236** parameters<br>
        gonna analyse your eye Facial.
        ###
        """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload an eye", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type}
        st.write(file_details)
        with open(os.path.join(save_input_img,uploaded_file.name),"wb") as f: 
            f.write(uploaded_file.getbuffer())         
            st.success("Saved File") 
        

    if uploaded_file is not None:
            img_file = uploaded_file
            image_load = Image.open(img_file)
            st.image(uploaded_file, width=100)

    #st.set_option('deprecation.showfileUploaderEncoding', False)


    if st.button('🩺 Analyse it'):
       with st.spinner('Making Prediction now...'):
	           time.sleep(11)


with row1_2:
    if uploaded_file is None:
        st.image('./img/bg-img.gif')
        #st.write('Waiting for your upload')
        st.markdown('''
            #
            #####
            ''')
        time.sleep(11)    
    # with st.spinner('Making Prediction now...'):
    #     time.sleep(4)
        #st.image('img/gif-to-jpeg.jpg')
        
    if  uploaded_file is not None:
        #st.image('./img/bg-img.gif')
        #st.write('Waiting for your upload')
        st.markdown("""---""")
        st.markdown('''
            ###  --- **processing image input Analysing**...
            #####
            ''')

        # Add a placeholder
        #latest_iteration = st.empty()
        #bar = st.progress(1)
        with st.spinner('--- **Making Per-Processing now**...'):
             time.sleep(4)
        list_ = ['- Resizing...', '- Compute image to number...', '- Features Extraction...', '- Neural Analysis...']
        bar = st.progress(0.00002)
        for i  in list_:
            # Update the progress bar with each iteration.
            st.text( i + '  ✓')
            time.sleep(0.5)
        st.markdown("""
                #####
                """)
        files = glob.glob(os.path.join(save_input_img, '*'))
        max_file = max(files, key=os.path.getctime)
        print(max_file)
        #img_file = uploaded_file
        image_load = Image.open(max_file)
        src = cv2.imread(max_file, cv2.IMREAD_UNCHANGED)
        img=cv2.resize(src,(IMAGE_SIZE,IMAGE_SIZE))
        #img = get_img_array(latest_file,32)
        model= load_cnn_model(model_path)
        def final_pred():
            proba = model.predict(img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3))
            output = np.argsort(proba[0],kind ='heapsort', axis = -1)[:-5:-1]
            make_prediction(output,proba)
            #n pred
        #resutlts=final_pred()
        with st.spinner('--- ✅ Making Prediction now...'):
             time.sleep(10)
        st.markdown("""
            ###   --- **Final-Step Result**:
            #####
            """)
        final_pred() 
        # new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 42px;">{final_pred()}</p>'
        # st.markdown(new_title, unsafe_allow_html=True)
        #final_pred().as_html()
        #st.markdown(pred.as_html(), unsafe_allow_html=True) 
        #st.success('Your loan is {}'.format(result))   
        #st.success(f"The predicted result is {resutlts}")
        #st.image(uploaded_file, width=50)
        st.markdown('''
            ##
            #####
            ''')
        st.text('''
            👈🏿 Don't hesitate to upload another one !
            ''')
        st.markdown('''
            #
            #####
            ''')
components.html(
    """
        <link href="assets/css/test.css" rel="stylesheet">
        <p class='LILOL' style="text-align: center;font-size: 11px;font-family: sans-serif;">Made by <a  target= "_blank" style="color: black;text-decoration: none;font-weight: 600;">Fouzia</a> - <a target= "_blank" style="color: black;text-decoration: none;font-weight: 600;">univesity name </a> - <a  target= "_blank" style="color: black;text-decoration: none;font-weight: 600;">PFE</a> @ year Project 2022</p>
    """,
    height=40,
)