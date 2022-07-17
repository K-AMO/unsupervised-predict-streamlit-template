"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

from PIL import Image

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    #st.title("Data Chronicles")

    image = Image.open('resources/imgs/clogo.jpeg')
    st.image(image, caption='Company logo')
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    #page_selection = st.sidebar.selectbox("Choose Option", page_options)
    #if page_selection == "Recommender System":
        # Header contents
   
    st.write('## Who are we!!')
    
    
        
    st.balloons()    
    st.markdown(" At Data Chronicles we consider ourselves your partners, and we take care of your technology so that you can focus on your customers’ needs. The goal of every member of our team of") 
    st.markdown(" over 4 000 people is to maximise your productivity, increase your profits, and most of all, futureproof your business. Data Chronicles offers a complete service in Information and")
    st.markdown(" Communications Technology (ICT). We take care of your technology so that your workforce is free to focus on your customers’ needs, build productivity, grow profits, and embark on 		the") 
    st.balloons() 
    st.markdown(" journey to Digital Transformation.Our track record of reliability, stability and consistency speaks for itself. Before Telkom’s acquisition of the company in 2015, The company had 		been running since") 
    st.markdown(" over 4 000 people is to maximise your productivity, increase your profits, and most of all, futureproof your business. Data Chronicles offers a complete service in Information and") 
    st.markdown(" 2005, when it was founded by twin brothers Adam and Chris Smith. The company was listed on the Johannesburg Stock Exchange (JSE) in 2010. Today we work with businesses from")
    st.markdown(" tiny start-ups to JSE-listed enterprises and international corporations.")
    st.balloons() 
        #st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        #st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        #sys = st.radio("Select an algorithm",
         #              ('Content Based Filtering',
          #              'Collaborative Based Filtering'))

        # User-based preferences
        #st.write('### Enter Your Three Favorite Movies')
        #movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        #movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        #movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        #fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        #if sys == 'Content Based Filtering':
           # if st.button("Recommend"):
               # try:
                 #   with st.spinner('Crunching the numbers...'):
                    #    top_recommendations = content_model(movie_list=fav_movies,
                                                            #top_n=10)
                   # st.title("We think you'll like:")
                   # for i,j in enumerate(top_recommendations):
                    #    st.subheader(str(i+1)+'. '+j)
                # except:
                  #  st.error("Oops! Looks like this algorithm does't work.\
                       #       We'll need to fix it!")


        #if sys == 'Collaborative Based Filtering':
         #   if st.button("Recommend"):
          #      try:
           #         with st.spinner('Crunching the numbers...'):
            #            top_recommendations = collab_model(movie_list=fav_movies,
             #                                              top_n=10)
              #      st.title("We think you'll like:")
               #     for i,j in enumerate(top_recommendations):
                #        st.subheader(str(i+1)+'. '+j)
                #except:
                 #   st.error("Oops! Looks like this algorithm does't work.\
                  #            We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    #if page_selection == "Solution Overview":
       # st.title("Solution Overview")
        #st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    st.balloons() 


if __name__ == '__main__':
    main()
