import streamlit as st
from datetime import date
from dates import dateValue
st.markdown("""
<style>
div.stButton:has(button[key="return_btn"]) > button {
    background-color:red;
    color: white;
    font-size: 18px;
    font-weight: 700;
    border-radius: 12px;
    width: 180px;
    height: 70px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div.stButton:has(button[key="small"]) > button {
    width: 180px;
    height: 70px;
    font-size: 18px;
    font-weight: 600;
    border-radius: 12px;
    background-color: #FFEEDD;
}
</style>
""", unsafe_allow_html=True)
def online():
    if "selected_name" not in st.session_state:
         st.session_state.selected_name = None

   
    names=["saloon A","Saloon B","saloon C"]
    if st.session_state.selected_name is None:
        for name in names:

            if st.button(name):
                
                st.session_state.selected_name=name
                st.session_state.current_page="date"
                #st.session_state.selected_page
                st.rerun()
        st.divider()        
        if st.button("return",type="primary"):
                
                st.session_state.selected_name = None
                st.session_state.sub_page="Appointment"
                st.session_state.current_page="appointment"  
                st.rerun()       
         
       
def offline():
    if "selected_name" not in st.session_state:
         st.session_state.selected_name = None

   
    names=["saloon A","Saloon B","saloon C"]
    if st.session_state.selected_name is None:
        for name in names:

            if st.button(name):
                
                st.session_state.selected_name=name
                st.session_state.current_page="offdate"
                #st.session_state.selected_page
                st.rerun()
        st.divider()        
        if st.button("return",type="primary"):
         
            st.session_state.selected_name = None
            st.session_state.sub_page="Appointment"  
            st.session_state.current_page="appointment"
            st.rerun()
       