import streamlit as st
from datetime import date

def dateValue(name):
    st.write(f"select a date for saloon {name}")
    selected_date = st.date_input(
                    "available appointment dates",min_value=date.today())  
    st.button("submit")  
    st.divider()                      
    if st.button("return",type="primary"):
            st.session_state.selected_page = None
            st.session_state.selected_name = None
            st.session_state.current_page="online"  
            st.rerun() 