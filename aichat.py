import os

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

    generic_template="get the list of top 10 saloons as per location name and review with contact info:"
    prompt=ChatPromptTemplate.from_messages(
        [("system",generic_template),("user","{text}")]
    )
    #res=prompt.invoke({"text":"find the top sloons near surathkal"})
    chain=prompt|model|parser
    result=chain.invoke({"text":input_text})
    return result