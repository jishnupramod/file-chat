import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import tempfile

def main():

    load_dotenv()

    st.set_page_config(page_title="File Chat 📑")
    st.header("File Chat 📑")
    csv_file = st.file_uploader("Drop your CSV file here", type="csv")

    if csv_file:

        # creating tempfile
        csv_contents = csv_file.read()

        with tempfile.NamedTemporaryFile(mode="wb", delete=False) as csv_temp_file:
            csv_temp_file.write(csv_contents)
            csv_temp_path = csv_temp_file.name
        
        csv_query = st.text_input("Chat with your CSV file: ")
        
        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, csv_temp_path, verbose=True)

        if csv_query:
            st.write(f"Your query is {csv_query}...\nWait for the answer...\n")
            response = agent.run(csv_query)
            st.write(response)


if __name__ == "__main__":
    main()