from langchain_google_genai import ChatGoogleGenerativeAI
import json
import os
from .prompt_helpers.knowledge_graph_prompt_helper.extract_name_entities_prompt_helper import named_entity_prompt

api_key = "AIzaSyBq2_GdMf0KhowSVSb0hn4Z_8B81kBewXY"
os.environ["GOOGLE_API_KEY"] = api_key
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


def get_ner_labels_from_llm(text):
    prompt = named_entity_prompt.format(text=text)

    try:
        response = llm.invoke(prompt)
        llm_output = response.content.strip()
        try:
            llm_entities = json.loads(llm_output)
            return llm_entities

        except json.JSONDecodeError:
            print(f"Error decoding JSON from LLM: {llm_output}")
            return []
    except Exception as e:
        print(f"Error calling Google Gemini API: {e}")
        return []
