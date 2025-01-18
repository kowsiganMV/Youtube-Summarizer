from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import re

#llama-3.2-11b-vision-preview
def LLM(subs):
    chat = ChatGroq(temperature=0, groq_api_key="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", model_name="llama-3.2-11b-vision-preview")

    lang_code="en"
    sub = subs
    subs=str(sub)
    prompt_extract=PromptTemplate.from_template(
        """ 
        <Title>
        You are an expert in [CATEGORY]. Below is a YouTube video transcript in JSON format. 
        Your task is to analyze the transcript and generate detailed notes for every topic or idea explained in the video. 
        Ensure no key point is missed, and elaborate on each idea with clarity and depth. 
        The notes should be organized, comprehensive, and tailored to an audience interested in [CATEGORY]. 
        Here's the transcript:{subs}
        """
        )   
    chain_extract= prompt_extract | chat
    res=chain_extract.invoke(input={"lang_code":lang_code,"subs":subs})
    return res

