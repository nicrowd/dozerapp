import streamlit as st
import pandas as pd
import base64

# Function to download data
def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="drinkogniser_responses.csv">Download and email us your choices as attached file</a>'
    return href

def main():
    st.title("Drinkogniser")

    with st.form("user_info_form"):
        name = st.text_input("Specify your name")
        email = st.text_input("Enter your email")
        design_option = st.selectbox("Select your 'drinkorganiser' design", 
                                     ["Wedding", "Birthdays", "Kids Party", "Design 4"])
        selected_color = st.color_picker("Pick a color for the design", '#00f900')
        
        # Form submission
        submitted = st.form_submit_button("Submit")
        if submitted:
            user_data = {
                "Name": name,
                "Email": email,
                "Design": design_option,
                "Color": selected_color
            }
            df = pd.DataFrame([user_data])
            st.write(df)
            st.markdown(get_table_download_link(df), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
