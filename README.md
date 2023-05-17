# Medical_Application_Streamlit
this repo contain the full the project DL with Web appplication using Streamlit for deployment 

### Installation 

i provided the Docker Image to run Directly which contain all the app requimemnts ,
to run the Docker images following command :

    ```sh 
        docker pull ghcr.io/deep-matter/streamlit:latset 
    ```
    ```sh
        docker run -i -t streamlit:latset
    ```
### Model Traning 

here we used Convolution Neual network to develope a model for predicting the signs of patient based on the Eyes from Images the code can found in Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1o7USeyjTLjmgjjGXkQLt96HYNAbc_r7j]

### Docker-Compose 

also you can run app using docker-compose command follwing you need to keep docker-compose.yml in root folder 

    ```sh
        docker-compose up 
    ```


