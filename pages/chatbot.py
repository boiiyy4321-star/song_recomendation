import os
import streamlit as st
import google.genai as genai


st.title("Ask FictionFinder! 📚")
st.write("Chat with our AI assistant to get personalized novel recommendations based on your preferences and mood. Just ask away!")


def load_env_file(env_path: str) -> None:
    if not os.path.exists(env_path):
        return
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and value and key not in os.environ:
                os.environ[key] = value

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
env_path = os.path.join(project_root, ".env")
load_env_file(env_path)

GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error(
        "Gemini API key not found. Please add `GEMINI_API_KEY` to `.streamlit/secrets.toml`, put it in `.env`, or set the environment variable `GEMINI_API_KEY`."
    )
    st.stop()

client = genai.Client(api_key=GEMINI_API_KEY)


instruksi_sistem = """
You are a friendly Bookworm AI, a highly expert novel recommendation assistant who knows almost every book in the world.Your task is to help users choose the perfect novel to read based on their current mood and genre preferences.Use a casual, engaging, and trendy youth-slang tone in your responses to keep things exciting and fun.You are FREE to recommend any famous, real-life novel in the world based on the user's preferences, genre, or mood.Provide interesting details for each book, including its title, author, and a compelling reason why it is absolutely worth reading.
"""


if "riwayat_chat" not in st.session_state:
    st.session_state.riwayat_chat = [
        {"role": "assistant", "teks": "Hey gng, Looking for a fun novel to read? What's your mood today? What genre are you looking for (Fantasy, Romance, or Mystery)?"}
    ]

# Tampilkan kembali semua pesan lama ke layar
for pesan in st.session_state.riwayat_chat:
    with st.chat_message(pesan["role"]):
        st.markdown(pesan["teks"])

pertanyaan = st.chat_input("What novel you wanna read today?")

if pertanyaan:

    with st.chat_message("user"):
        st.markdown(pertanyaan)
    st.session_state.riwayat_chat.append({"role": "user", "teks": pertanyaan})

   
    konteks_obrolan = instruksi_sistem + "\n\nRiwayat Obrolan:\n"
    for msg in st.session_state.riwayat_chat:
        konteks_obrolan += f"{msg['role']}: {msg['teks']}\n"


    with st.chat_message("assistant"):
        with st.spinner("Finding the best recommendation for you..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=konteks_obrolan
                )
                jawaban = response.text
            except Exception as e:
                jawaban = f"NO! There's an error in the system: {e}"
            
            st.markdown(jawaban)

   
    st.session_state.riwayat_chat.append({"role": "assistant", "teks": jawaban})
