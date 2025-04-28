from dotenv import load_dotenv
load_dotenv()
import os
# from langchain_community.llms import ollama
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser


## langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]=os.getenv("LANGCHAIN_TRACING_V2")


## setting up the prompt tempalte
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You're a help assistant. Respond in easy way of the asked Questions "),
        ("user","question:{question}")
    ]
)


## setting up llm model
llm=Ollama(model="llama3")
outputparser=StrOutputParser()
chain= prompt|llm|outputparser


## Setting up straemlit framework

st.title("Langchain with llama3")
input_text=st.text_input("what question in your mind")



if input_text:
    output=chain.invoke({"question":input_text})
    st.write(output)
