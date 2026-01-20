import streamlit as st

st.set_page_config(
    page_title="Conversational Geospatial Assistant",
    layout="wide"
)
def init_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "agent_mode" not in st.session_state:
        st.session_state.agent_mode = "Intent Based Place Discovery"

    if "agent_status" not in st.session_state:
        st.session_state.agent_status = "idle"

    if "tool_logs" not in st.session_state:
        st.session_state.tool_logs = []

    if "memory" not in st.session_state:
        st.session_state.memory = {}

init_state()

def run_agent(user_input, agent_mode):
    st.session_state.agent_status = "thinking"

    reasoning_steps = [
        "Parsed user query",
        "Detected experiential intent",
        "Identified location reference",
        "Planned geospatial strategy"
    ]

    st.session_state.agent_status = "acting"

    response = (
        f"**{agent_mode}** engaged.\n\n"
        "I’ve understood your intent and "
        "identified relevant geospatial actions."
    )

    st.session_state.agent_status = "done"

    return response, reasoning_steps


st.sidebar.title("Agent Mode")
st.sidebar.markdown("Intent Based Place Discovery")
# agent_mode = st.sidebar.selectbox(
#     "Select Agent",
#     [
#         "Semantic Place Discovery",
#     ]
# )
agent_mode = "Intent Based Place Discovery"

st.sidebar.markdown("---")

st.sidebar.markdown("### Project Context")
st.sidebar.write(
    "MapmyIndia\n"
    "Generative AI for Geospatial Intelligence"
)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent_mode" not in st.session_state:
    st.session_state.agent_mode = "Intent Based Place Discovery"

if "agent_status" not in st.session_state:
    st.session_state.agent_status = "idle"

if "tool_logs" not in st.session_state:
    st.session_state.tool_logs = []

if "memory" not in st.session_state:
    st.session_state.memory = {}


st.title("Conversational Map Intelligence")

st.caption(
    "Understand natural language, intent, and emotion "
    "to perform geospatial reasoning"
)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input(
    "Ask naturally (English / Hindi / Hinglish)..."
)

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.status("Agent Status", expanded=True) as status:

            status.update(label="Thinking...", state="running")

            reply, reasoning = run_agent(
                user_input,
                st.session_state.agent_mode
            )

            status.update(label="Acting...", state="running")

            st.write(reply)

            with st.expander("Agent Reasoning (Explainable)"):
                for step in reasoning:
                    st.write("•", step)

            status.update(label="Done", state="complete")

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
