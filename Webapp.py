import streamlit as st
from streamlit_option_menu import option_menu
st.title("Parlour Page",text_alignment="center")
st.markdown("<h1 style='text-align: center; color:red;font-size:10px;'>Development of page layout as per flowchart(atlassian)</h1>", unsafe_allow_html=True)
st.set_page_config(layout="wide")
if "current_page" not in st.session_state:
    st.session_state.current_page="Home"
st.markdown("""
<style>

div.stButton > button { 
width: 360px; 
height: 220px; 
font-size: 22px; 
color: #000000; 
font-size: 100px; 
font-weight: 10000; 
border-radius: 20px; 
background-color: #FFDBBB; 
border: 2px solid #000000; 
} 
/* Hover effect */ 
div.stButton > button:hover { 
background-color: #FFDBBB;
 border-color: #000000;
}

</style>
""", unsafe_allow_html=True)

def near_me():
  
    st.write("list of parlours near me")
    
def appointment():
    st.write("contact info to book an appointment")
def category():   
    st.write("below options will show the sorted list of parlours based on price(optional can add other sorting options)")
    col1,col2,col3=st.columns(3)
    with col1:
         if st.button("hairstyle parlour"):
            st.write("list of hairstyle palours")
         
    with col2:     
         if st.button("spa"):
              st.write("list of spa palours")
    with col3:     
         if st.button("makeup parlour"):
                st.write("list of makeup palours")    

def home():
    selected=option_menu(
        menu_title=None,
        options=["Parlour Near Me","Book an Appointment","Categories"],
        icons=["geo-alt", "calendar", "list"],
        orientation="horizontal",
        default_index=0
    )
  
    if selected == "Parlour Near Me":
            near_me()
    if selected == "Book an Appointment":
            appointment() 

    if selected== "Categories":
            category()
            
             
if st.session_state.current_page == "Home":
    home()