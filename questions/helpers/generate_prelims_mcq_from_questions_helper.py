from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from ..helpers.prompt_helpers.mock_mcq_prompt_helper.single_statement_question_prompt_helper import \
    single_statement_question_prompt
from ..helpers.prompt_helpers.mock_mcq_prompt_helper.two_statements_question_prompt_helper import \
    two_statements_question_prompt
from ..helpers.prompt_helpers.mock_mcq_prompt_helper.three_statements_question_prompt_helper import \
    three_statements_question_prompt
from ..helpers.prompt_helpers.mock_mcq_prompt_helper.identify_features_question_prompt_helper import \
    identify_features_question_prompt
from ..helpers.prompt_helpers.mock_mcq_prompt_helper.match_the_pairs_question_prompt_helper import \
    match_the_pairs_prompt
import multiprocessing
from ..helpers import get_named_entities_from_text_helper as neh, query_kg_helper as qkh

os.environ["TOKENIZERS_PARALLELISM"] = "false"

api_key_1 = "AIzaSyCxTCYQO7s23L33kC4Io4G-i1p1ytD-OiI"
api_key_2 = "AIzaSyC_w68KVtMCloF5V3NKAUBp6EdhqcA0ylw"
api_key_3 = "AIzaSyAA39dIq31iDJR-i7mZRWEKhkVVIr1Bz4g"
api_key_4 = "AIzaSyD0nx9rH7HhQZDpJrY0hOaOR9Xok4r-liM"
api_key_5 = "AIzaSyBq2_GdMf0KhowSVSb0hn4Z_8B81kBewXY"


def traverse_graph_to_get_content(source_question):
    named_entities = neh.get_ner_labels_from_llm(source_question)
    p = []
    for entity in named_entities:
        print(entity)
        target_entity_text = entity['entity']
        all_paths = qkh.get_paths_from_entity_any_label(target_entity_text, max_depth=1)
        for path in all_paths:
            p.append(path)
    return p


def worker(prompt, prefix, suffix, api_key, source_question, target_content):
    query = prompt.format(source_question=source_question,
                          target_content=target_content)
    os.environ["GOOGLE_API_KEY"] = api_key
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    response = llm.invoke(query).content
    with open("temp/" + prefix + "_ " + suffix, "w") as output_file:
        output_file.write(response + "\n\n")


def generate_mock_mcq(source_question, target_embeddings_path, prefix):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/multi-qa-MiniLM-L6-cos-v1")
    target_vectorstore = FAISS.load_local(target_embeddings_path,
                                          embeddings=embeddings,
                                          allow_dangerous_deserialization=True)
    print(source_question)
    searched_content = target_vectorstore.similarity_search(source_question, k=10)
    target_content = traverse_graph_to_get_content(source_question)
    print(target_content)
    for doc in searched_content:
        target_content += "\n" + str(doc)
    for prompt, suffix, api_key in [(single_statement_question_prompt, "single_statement.txt", api_key_1),
                                    (two_statements_question_prompt, "two_statement.txt", api_key_2),
                                    (three_statements_question_prompt, "three_statement.txt", api_key_3),
                                    (identify_features_question_prompt, "identify_features.txt", api_key_4),
                                    (match_the_pairs_prompt, "match_the_pairs.txt", api_key_5)
                                    ]:
        processes = []
        p = multiprocessing.Process(target=worker,
                                    args=(prompt, prefix, suffix, api_key, source_question, target_content))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
