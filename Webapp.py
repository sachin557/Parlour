import streamlit as st
from streamlit_option_menu import option_menu
from appointment import online,offline
from dates import dateValue
from off_date import offDateValue
st.title("Parlour Page",text_alignment="center")
st.markdown("<h1 style='text-align: center; color:red;font-size:10px;'>Development of page layout as per flowchart(atlassian)</h1>", unsafe_allow_html=True)
st.set_page_config(layout="wide")
if "sub_page" not in st.session_state:
    st.session_state.sub_page = None
if "current_page" not in st.session_state:
    st.session_state.current_page="Home"
if "selected_name" not in st.session_state:
    st.session_state.selected_name = None

st.markdown("""
<style>
div.stButton:has(button[key^="small_"]) > button {
    width: 180px;
    height: 70px;
    font-size: 18px;
    font-weight: 600;
    border-radius: 12px;
    background-color: #FFEEDD;
}
</style>
""", unsafe_allow_html=True)

def near_me():
  
    st.write("list of parlours near me")
    
def appointment(page):
    col1,col2=st.columns(2)
    with col1:
        
        if st.button("Online appointment"):
            
            
            st.session_state.current_page="online"
            st.rerun()
            
    with col2:
        if st.button("Offline call appointment"):
            st.session_state.current_page="offline"
            st.rerun() 
    st.divider()  
    if page is not None:         
        if st.button("return",type="primary"):
            st.session_state.current_page="Home"
            st.rerun()       
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
def Guid():
    st.write("this a guid which will have complete guid and navigation details for user")
def home():
    
    selected=option_menu(
            menu_title=None,
            options=["Parlour Near Me","Book an Appointment","Categories","Guid"],
            icons=["geo-alt", "calendar", "list","book"],
            orientation="horizontal",
            default_index=0
        )
    
    if selected == "Parlour Near Me":
                near_me()
    if selected == "Book an Appointment":
                appointment(st.session_state.sub_page) 

    if selected== "Categories":
                category()
    if selected== "Guid":
                Guid()     
            
             
if st.session_state.current_page == "Home":
    home()
elif st.session_state.current_page == "online":
    online()   
elif st.session_state.current_page == "offline":
    offline()     
elif st.session_state.current_page=="date":
    dateValue(st.session_state.selected_name)  
elif st.session_state.current_page=="offdate":
    offDateValue(st.session_state.selected_name) 
elif st.session_state.current_page=="appointment":
    page=st.session_state.sub_page
    appointment(page)        