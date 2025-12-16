import streamlit as st
from datetime import date

def offDateValue(name):
    st.write(f"below is the contact details for the select a date for saloon {name}")
      
    st.divider()                      
    if st.button("return",type="primary"):
            st.session_state.selected_page = None
            st.session_state.selected_name = None
            st.session_state.current_page="offline"  
            st.rerun() 