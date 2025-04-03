from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from ..helpers.prompt_helpers.mock_mcq_prompt_helper.explanation_prompt_helper import \
    explanation_prompt
import multiprocessing
from ..helpers import get_named_entities_from_text_helper as neh, query_kg_helper as qkh

os.environ["TOKENIZERS_PARALLELISM"] = "false"

api_key_1 = "AIzaSyCxTCYQO7s23L33kC4Io4G-i1p1ytD-OiI"
api_key_2 = "AIzaSyC_w68KVtMCloF5V3NKAUBp6EdhqcA0ylw"
api_key_3 = "AIzaSyAA39dIq31iDJR-i7mZRWEKhkVVIr1Bz4g"
api_key_4 = "AIzaSyD0nx9rH7HhQZDpJrY0hOaOR9Xok4r-liM"
api_key_5 = "AIzaSyBq2_GdMf0KhowSVSb0hn4Z_8B81kBewXY"


def traverse_graph_to_get_content(source_content):
    named_entities = neh.get_ner_labels_from_llm(source_content)
    p = []
    for entity in named_entities:
        print(entity)
        target_entity_text = entity['entity']
        all_paths = qkh.get_paths_from_entity_any_label(target_entity_text, max_depth=3)
        for path in all_paths:
            p.append(path)
    return p


def worker(prompt, api_key, source_content, question):
    query = prompt.format(question=question,
                          target_content=target_content)
    os.environ["GOOGLE_API_KEY"] = api_key
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    response = llm.invoke(query).content
    with open("temp/explanation", "a+") as output_file:
        output_file.write(response + "\n\n")


def generate_mock_mcq(question, source_embeddings_path):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/multi-qa-MiniLM-L6-cos-v1")
    source_vectorstore = FAISS.load_local(
        source_embeddings_path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True)
    source_content = str(traverse_graph_to_get_content(question))
    searched_content = source_vectorstore.similarity_search(question)
    for doc in searched_content:
        source_content += "\n" + doc.page_content
    worker(explanation_prompt, api_key_2, source_content, question)
    # for prompt, api_key in [api_key_1, api_key_2, api_key_3, api_key_4, api_key_5]:
    #     processes = []
    #     p = multiprocessing.Process(target=worker,
    #                                 args=(explanation_prompt, api_key, source_content, question))
    #
    #     processes.append(p)
    #     p.start()
    #     for p in processes:
    #         p.join()
