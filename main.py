# Setup
import streamlit as st
from scrape import (scrape_website, extract_body_content, clean_body_content, split_dom_content) # scrape.py
from parse import parse_with_ollama # parse.py

# Interface
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping...")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)
    

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing content...")
            dom_chunk = split_dom_content(st.session_state.dom_content)
            result=parse_with_ollama(dom_chunk, parse_description)
            st.write(result)

