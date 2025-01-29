from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

def LLM(subs, model_name="llama-3.2-11b-vision-preview", groq_api_key="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"):
    # Initialize ChatGroq instance
    chat = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name=model_name)

    # Define the prompt template
    prompt_extract = PromptTemplate.from_template(
        """
        <Title>
        You are an expert in analyzing YouTube video transcripts. Below is a transcript in JSON format. 
        Your task is to generate detailed notes for every topic or idea explained. 
        Ensure no key point is missed, and elaborate on each idea with clarity and depth. 
        Notes should be organized and tailored to an audience interested in the video content.
        Transcript: {subs}
        """
    )

    # Combine the prompt and chat model into a chain
    chain_extract = prompt_extract | chat

    # Invoke the chain with the transcript as input
    result = chain_extract.invoke(input={"subs": subs})
    return result


# Chunk with overlap to avoid missing data between chunks
def chunk_data(data, chunk_size):
    chunks = []
    start = 0
    while start < len(data):
        end = min(len(data), start + chunk_size)
        chunks.append(data[start:end])
        start += chunk_size
    return chunks

# Function to process large transcripts
def process_large_transcript(subs,chunk_size=1000):
    chunks = chunk_data(subs, chunk_size=chunk_size)
    results = []
    try:
        
        for i, chunk in enumerate(chunks):
            print(f"Processing chunk {i + 1}/{len(chunks)}...")
            
            result = LLM(chunk)
            # Extract the text content from the AIMessage object
            results.append(result.content)

        # Step 3: Combine all results into a single string
        combined_result = "\n".join(results)
        print(combined_result)
    except Exception as e:
        print(e)
    return combined_result

