import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance


# Title and Subheader
st.title("Data Understanding")
st.subheader("Data Understanding using Streamlit ")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")


df = pd.read_csv(DATA_PATH)
# st.dataframe(df)

# Show Dataset
if st.checkbox("Preview First Five Records"):
    st.write(df.head())
		
if st.checkbox("Preview Last Five Records"):
	st.write(df.tail())
	
# Show Description
if st.checkbox("Show All Column Names"):
	
	st.text("Columns:")
	st.write(df.columns)
	
# Data frame Dimensions
if st.checkbox("Show Dimensions"):
	st.write("Total Number Of Rows :",df.shape[0])
	st.write("Total Number Of Columns :",df.shape[1])

# Dataframe Summary	
if st.checkbox("Show Summary of Dataset"):
	st.write(df.describe())
	

	
	
	
	


