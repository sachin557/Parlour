import os
import re
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
def chatbot(Groq_api,input_text):
    model=ChatGroq(model="llama-3.1-8b-instant",groq_api_key=Groq_api)
    #messages=[
       # SystemMessage(content="list the saloons by top ranking and their contact info based on given location"),
        #HumanMessage(content="saloons near the location")
    #]
    #result=model.invoke(messages)
    parser=StrOutputParser()
   # chain=model|parser
    #out=chain.invoke(messages)

    generic_template="""get the list of top 10 saloons as per location name and best review with contact info like:
    1)saloon name
    2)contact info
    3)google rating
    4)Address
    5)Google Maps link using:
     https://www.google.com/maps/search/?api=1&query=<saloonName+address>"""
    prompt=ChatPromptTemplate.from_messages(
        [("system",generic_template),("user","{text}")]
    )
    #res=prompt.invoke({"text":"find the top sloons near surathkal"})
    chain=prompt|model|parser
    result=chain.invoke({"text":input_text})
    return result
def get_map_link(Groq_api,saloon_name,address):
        up_saloon_name=re.sub(r"[^A-Z a-z]","",saloon_name)
        updated_saloon_name=up_saloon_name.replace(" ","+") if " " in up_saloon_name else up_saloon_name
        address=re.sub(r'\d+',"",address).replace(" ","+") 
        link=f"https://www.google.com/maps/search/?api=1&query={updated_saloon_name}+{address}"
        return link