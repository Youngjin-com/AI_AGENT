import streamlit as st
from langsmith import uuid7

from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver

# models
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

# custom tools
from tools.fetch_qa_content import fetch_qa_content
from tools.fetch_stores_by_prefecture import fetch_stores_by_prefecture


CUSTOM_SYSTEM_PROMPT = """
당신은 한국의 저가 이동통신사 ‘영진모바일’의 고객지원(CS) 담당자입니다.

[역할]
- 자사 서비스와 휴대전화 관련 질문에만 성실하고 정확하게 답변합니다.
- 그 외 주제의 질문에는 정중히 사양합니다.

[답변 규칙]
- ‘영진모바일’에 관한 질문을 받으면 반드시 툴을 사용해서 답변을 찾으세요.
- 고객이 사용한 언어로 답변하세요. (예 영어 질문 → 영어 답변)
- 불분명한 점이 있으면 먼저 고객에게 확인하세요.
- 의도를 충분히 파악할 때까지 섣불리 답변하지 마세요.
- "지점은 어디에 있나요?"와 같은 질문에는 바로 답변하지 말고, 
   먼저 거주 지역을 물어본 후 맞춤 안내를 제공하세요.
"""


def init_page():
    st.set_page_config(page_title="고객 지원", page_icon="🐻")
    st.header("고객 지원🐻")
    st.sidebar.title("옵션")


def init_messages():
    clear_button = st.sidebar.button("대화 초기화", key="clear")
    if clear_button or "messages" not in st.session_state:
        welcome_message = (
            "영진모바일 고객지원에 오신 것을 환영합니다. 질문을 입력해 주세요🐻"
        )
        st.session_state.messages = [{"role": "assistant", "content": welcome_message}]
        st.session_state["checkpointer"] = InMemorySaver()
        st.session_state["thread_id"] = str(uuid7())


def select_model(temperature=0):
    models = ("GPT-5.2", "Claude Sonnet 4.5", "Gemini 2.5 Flash")
    model = st.sidebar.radio("사용할 모델 선택:", models)
    if model == "GPT-5.2":
        return ChatOpenAI(temperature=temperature, model="gpt-5.2")
    elif model == "Claude Sonnet 4.5":
        return ChatAnthropic(
            temperature=temperature, model="claude-sonnet-4-5-20250929"
        )
    elif model == "Gemini 2.5 Flash":
        return ChatGoogleGenerativeAI(temperature=temperature, model="gemini-2.5-flash")


def create_customer_support_agent():
    tools = [fetch_qa_content, fetch_stores_by_prefecture]
    llm = select_model()

    summarization_middleware = SummarizationMiddleware(
        model=llm,
        trigger=("tokens", 8000),
        keep=("messages", 10),
    )

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=CUSTOM_SYSTEM_PROMPT,
        checkpointer=st.session_state["checkpointer"],
        middleware=[summarization_middleware],
        debug=True,
    )

    return agent


def main():
    init_page()
    init_messages()
    agent = create_customer_support_agent()
    config = {"configurable": {"thread_id": st.session_state["thread_id"]}}

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder="법인 명의로 계약이 가능한가요?"):
        st.chat_message("user").write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("답변 생성 중..."):
                result = agent.invoke({"messages": [("user", prompt)]}, config)
            answer = result["messages"][-1].content
            st.write(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()
