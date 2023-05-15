![Scarp_data from search engine](./image_readm/download.png)


# 🧐 Project philosophy

# Check Samples dataset and collecting 
* fisrt probelm we had . it was the data to use in our task : \\
the data wasn't avaialble from comfirme Organization because of the authourization , here we decide to use automated web scapring data to collect sample from search engine like " Google " , and we know this technics has some issues to be consider we will list them 
1. unbalnace dataset 
2. high varainces between classes collected 
3. random scaraped images based one queries 
* solution to fixed the problem we decribed 
1. we did the maunally deleted the unnecessary images from each folder's class 
2. we used augementation technic to balance the dataset and change images to multi-shape repesentation to make data be more usefull to feed into model 
3. for solve the variance we try to use augmemtation layer to random let model learn from diffrent postional at data distrution 
* here we will display few samples 
* convert dataset from directory setup into dataFrame


# ✍️ Requirements for this project  to run
* install python version 3.9 from officiel website 
* creat Envs install virtualenv to allow creating env
     pip install virtualenv
     - creat env follwoing this step by runing this commands on cmd or anaconda peromet 
         1. virtualenv scrap_data
         2. cd scrap_data\Scripts
         3. source ./activate or ./activate 

* run this command line 
   pip install -r requirements.txt 
* run each script indeviadial for getting the results 
       - python scarping.py 
       - python image_crop.py
       - python augmetation.py 


# ⚠️ License

is for final etude project master Big data Fouzia git 

<br />

---

<br />

# 💛

Reminder that *you are great, you are enough, and your presence is valued.* 