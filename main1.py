import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from llm_helper import generate_hashtags

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish", "Minglish"]
tone_options = ["Professional", "Motivational", "Humorous"]

def main():
    st.subheader("LinkedIn Post Generator")
    fs = FewShotPosts()
    tags = fs.get_tags()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        selected_tag = st.selectbox("Topic", options=tags)
    with col2:
        selected_length = st.selectbox("Length", options=length_options)
    with col3:
        selected_language = st.selectbox("Language", options=language_options)
    with col4:
        selected_tone = st.selectbox("Tone", options=tone_options)

    if st.button("Generate"):
        post = generate_post(
            length=selected_length,
            language=selected_language,
            tag=selected_tag,
            tone=selected_tone
        )
        hashtags = generate_hashtags(post, language=selected_language)
        st.write(post)
        st.markdown("**Hashtags:** " + ", ".join(hashtags))

if __name__ == "__main__":
    main()
