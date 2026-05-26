import streamlit as st

st.set_page_config(
    page_title="NovelFinder", 
    page_icon="📚", 
    layout="wide"  # Changed to wide layout for more structured content space
)

def home_page() -> None:
    # --- HERO SECTION ---
    st.title("📚 Welcome to NovelFinder!")
    st.subheader("Your ultimate gateway to finding your next favorite book.")
    st.markdown(
        "Whether you know exactly what vibe you are looking for or want an AI assistant "
        "to guide your path, NovelFinder has you covered."
    )
    
    st.info(" **Quick Start Guide:** Use the sidebar on the left to seamlessly switch between our discovery modules!")
    st.divider()

    # --- METRICS / STATS SECTION ---
    st.write("### ✨ Current Catalog Highlights")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Total Real-Life Novels Indexed", value="1,200+", delta="Updated Today")
    with m2:
        st.metric(label="Genres Explored by AI", value="14 Genres", delta="Growing")
        
    st.divider()

    # --- FEATURE TEASERS SECTION ---
    st.write("### 🧭 Discover Our Tools")
    col_rec, col_bot = st.columns(2)
    
    with col_rec:
        st.markdown("#### ⭐ Top Recommendations")
        st.write(
            "Skip the searching. Go straight to our curated directory of critical masterpieces. "
            "Every book here carries an exceptionally high rating with detailed synopsis cards."
        )
        st.caption("👉 Click *Top Recommendation* in the sidebar to view.")

    with col_bot:
        st.markdown("#### 🤖 FictionFinder AI Chatbot")
        st.write(
            "Have a highly specific storyline mood in mind? Talk directly with FictionFinder, "
            "our dedicated AI assistant trained to hunt down hidden literary gems tailored to your prompt."
        )
        st.caption("👉 Click *FictionFinder* in the sidebar to chat.")

    st.divider()

    # --- POPULAR GENRES GRID ---
    st.write("### 🏷️ Explore Popular Genres")
    g1, g2, g3, g4 = st.columns(4)
    with g1:
        st.button("🔮 Fantasy", use_container_width=True)
    with g2:
        st.button("🚀 Sci-Fi", use_container_width=True)
    with g3:
        st.button("💖 Romance", use_container_width=True)
    with g4:
        st.button("🔍 Thriller", use_container_width=True)

# --- SIDEBAR CONFIGURATION ---
st.sidebar.title("NovelFinder")
st.sidebar.write("Find Your Next Read!")
st.sidebar.divider()
st.sidebar.caption("v1.1.0 • Built with Streamlit")

# --- NAVIGATION ROUTING ---
pages = [
    st.Page(home_page, title="Home", default=True),
    st.Page("pages/recommendation.py", title="Top Recommendation"),
    st.Page("pages/chatbot.py", title="FictionFinder")
]

pg = st.navigation(pages)
pg.run()