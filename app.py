import streamlit as st
import os
from document_processor import *
from classifier import *

st.title("Cloud-Based Document Analytics")

uploaded_files = st.file_uploader("Upload PDF or DOCX files", accept_multiple_files=True)

if uploaded_files:
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    local_paths = []
    for uploaded in uploaded_files:
        path = os.path.join("uploads", uploaded.name)
        with open(path, "wb") as f:
            f.write(uploaded.getbuffer())
        local_paths.append(path)

    st.subheader("Sorted Documents")
    sorted_paths = sort_documents_by_title(local_paths)
    for path in sorted_paths:
        st.write(path)

    keyword = st.text_input("Enter keyword to search")
    if keyword:
        for path in local_paths:
            results = search_in_document(path, keyword)
            if results:
                st.markdown(f"**{os.path.basename(path)}** contains '{keyword}'")

    st.subheader("Classification")
    text_data = ["example document about physics", "legal contract content"]
    labels = ["Science", "Law"]
    model = train_classifier(text_data, labels)
    for path in local_paths:
        content = extract_text_from_document(path)
        if content:
            label = predict_category(model, content)
            st.write(f"{os.path.basename(path)} classified as: {label}")
