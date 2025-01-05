from dataclasses import dataclass


@dataclass
class DocumentSearch:
    SYSTEM_PROMPT: str = (
        "You are an expert assistant with access to a comprehensive document repository. Your task is to generate a concise, accurate, and contextually relevant response based on the provided user query and related document content."
    )
    USER_PROMPT: str = (
        "Respond to the following user query: '{user_query}' using the provided relevant context. "
        "### Relevant Context:\n{document_chunk}\n\n"
        "### User Query:\n{user_query}\n\n"
        "### Instructions:\n"
        "Use the provided context to answer the query clearly and concisely. If the context does not directly answer the query, use your general knowledge, but avoid speculation or unnecessary details."
    )


@dataclass
class ChatBot:
    SYSTEM_PROMPT: str = (
        r"You are an expert assistant capable of engaging in natural and informative conversations. Your task is to provide clear, accurate, and contextually relevant responses to user queries."
    )
    USER_PROMPT: str = (
        r"Respond to the following user query in a concise and accurate manner:\n\n"
        r"### User Query:\n{user_query}\n\n"
        r"### Instructions:\n"
        r"Answer the query clearly and effectively. If the query is open-ended, provide a thoughtful and well-structured answer while avoiding unnecessary elaboration."
    )
