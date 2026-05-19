import streamlit as st
import re

st.set_page_config(page_title="UPSC MCQ Formatter", page_icon="📝")
st.title("📄 UPSC MCQ Formatter")
st.markdown("Upload your wrongly formatted file → Get correctly formatted file instantly")

uploaded_file = st.file_uploader("Choose a .txt file", type=['txt'])

if uploaded_file is not None:
    content = uploaded_file.read().decode('utf-8')
    
    # Split into lines
    lines = content.split('\n')
    formatted_lines = []
    i = 0
    
    while i < len(lines):
        current_line = lines[i]
        formatted_lines.append(current_line)
        
        # Check if this line ends with colon (question intro) and next line is empty
        if i + 1 < len(lines):
            next_line = lines[i + 1]
            # If current line has a colon and ends a question intro, and next line is empty
            if ':' in current_line and (current_line.strip().startswith('Q') or 'consider the following' in current_line.lower()):
                if next_line.strip() == '':
                    # Skip the blank line (do NOT add it)
                    i += 1
        i += 1
    
    formatted_content = '\n'.join(formatted_lines)
    
    st.success("✅ File formatted successfully!")
    st.download_button(
        label="📥 Download Corrected File",
        data=formatted_content,
        file_name="corrected_mcqs.txt",
        mime="text/plain"
    )
    
    with st.expander("Preview (first 2000 characters)"):
        st.text(formatted_content[:2000])
else:
    st.info("👆 Please upload a .txt file to begin")

st.markdown("---")
st.caption("Removes blank lines between question intro and numbered statements. Preserves blank lines after Ex: explanations.")