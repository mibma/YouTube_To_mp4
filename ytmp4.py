from pytube import YouTube
import streamlit as st
import tkinter as tk
from tkinter import filedialog

def download(url,path):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res=streams.get_highest_resolution()
        highest_res.download(output_path=path)
        
        print("Video downloaded ")
        
        
    except Exception as e:
        print(e)   


def openfile():
    folder=filedialog.askdirectory()
    if folder:
        print(f"Selected folder : {folder}")
        
    return folder    
    

if __name__=="__main__":
    st.title("Youtube Video Downloader ")
  
    url=st.text_input("Enter Youtube Video url ")
    path=st.text_input("Enter the location where you want to save ")
    
   
    
    
    if st.button("Download mp4 "):
        if url:
            
            download(url,path=path)
            st.success("Downloading ")
        else: 
            st.warning("Please enter a url and select a valid loactaion") 
               
            

    

        