from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def build_rag_chain(llm, retriever):
    contextual_prompt = ChatPromptTemplate.from_messages([
        ("system", "Formulate a standalone question from chat history."),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextual_prompt)

    answer_prompt = ChatPromptTemplate.from_messages([
        ("system", "Use the retrieved context to answer the question.\n{context}"),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])
    qa_chain = create_stuff_documents_chain(llm, answer_prompt)
    return create_retrieval_chain(history_aware_retriever, qa_chain)
