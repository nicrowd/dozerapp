import streamlit as st
import pandas as pd
import base64

# Function to download data
def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="drinkogniser_responses.csv">Download and email us your choices as attached file</a>'
    return href


# Set up the page

st.set_page_config(page_title="Track your drink with Drinkogniser", 
                   page_icon=':partying_face:',
                   layout='centered',
                   )


header_image = 'images/dozer_front.png'

st.image(header_image, use_column_width=True)


st.subheader("The Ultimate Drink Identification Solution!")

st.info("""
        Ever found yourself at a party, meeting, or conference, 
        sipping from a glass and suddenly wondering, "Is this really my drink?" 
        Worry no more! The Drinkogniser is here to keep track of your beverage.        
        """)


# Product Display in a container with a horizontal layout
with st.expander(":man_dancing: Introducing Drinkogniser!"):
    st.markdown("""
             🌟 Unique & Stylish: Our tags are not just functional, 
             they're a fashion statement! 
             With an array of vibrant colors and trendy designs, 
             your drink won’t just stand out, it’ll make a statement.

            🥂 Versatile for Every Occasion: Whether it's a frothy pint at a 
            bustling party, a sleek bottle at a formal business meeting, 
            or a sophisticated wine glass at a casual get-together, 
            Drinkogniser fits them all with ease.

            👥 Perfect for Social Gatherings: Make mingling a breeze! 
            With Drinkogniser, you’ll spend less time guessing which drink 
            is yours and more time enjoying conversations. 
            It's a social butterfly's best friend.

            🔒 Safe and Secure: Our tags are designed to snugly fit your drink,
            ensuring they stay in place no matter how lively the event gets.
            
            💡 Ideal for Everyone: Whether you're hosting a party, 
            attending a conference, or organizing a corporate event, 
            Drinkogniser adds a touch of personalization and practicality.
            
            🥳 Special Launch Offer: Order now and be among the first to 
            elevate your social experience with Drinkogniser. 
            Your drink, your style, your way!
            
             
             """
             )

# Product Display in a container with a horizontal layout
with st.expander(":screwdriver: How to use Drinkogniser?"):
    # Images are stored in a subfolder named 'images'
    product_images = ['images/bottle.png', 'images/can.png', 
                      'images/pint.png', 'images/wine.png']
    product_descriptions = ["Bottle", "Can", "Pint", "Wine"]

    # Create a column for each image
    cols = st.columns(4)
    for i, (img, desc) in enumerate(zip(product_images, product_descriptions)):
        with cols[i]:
            st.image(img, caption=desc)


# User Interaction
with st.expander(":screwdriver: Watch a Video!"):
    
    dozervideo = 'videos/Drinkogniser.mp4'
    
    st.video(dozervideo)


# # Create tabs for different events
# tab1, tab2, tab3, tab4, tab5 = st.tabs(["Wedding", 
#                                         "Birthday", 
#                                         "Kids Party", 
#                                         "Conference",
#                                         "Special Launch Event",
#                                   ])

# # Add content to the Wedding tab
# with tab1:
#     with st.expander("See Design Options"):
#         st.markdown(''':red[Wedding Drinkogniser Design Options]''')
#         design1 = st.select_slider(
#         'Select design options',
#         options=['Design A','Design B','Design C', 'Design D', 'Design E',],key='d1')
#         st.info(f'Your selected {design1}')

# # Add content to the Birthday tab
# with tab2:
#     with st.expander("See Design Options"):
#         st.markdown(''':red[Birthday Drinkogniser Design Options]''')
#         design2 = st.select_slider(
#         'Select design options',
#         options=['Design A','Design B','Design C', 'Design D', 'Design E',],key='d2')
#         st.info(f'Your selected {design2}')

# # Add content to the Kids Party tab
# with tab3:
#     with st.expander("See Design Options"):
#         st.markdown(''':red[Kids Party Drinkogniser Design Options]''')
#         design3 = st.select_slider(
#         'Select design options',
#         options=['Design A','Design B','Design C', 'Design D', 'Design E',],key='d3')
#         st.info(f'Your selected {design3}')

# # Add content to the Conference tab
# with tab4:
#     with st.expander("See Design Options"):
#         st.markdown(''':red[Conference Drinkogniser Design Options]''')
#         design4 = st.select_slider(
#         'Select design options',
#         options=['Design A','Design B','Design C', 'Design D', 'Design E',],key='d4')
#         st.info(f'Your selected {design4}')

# # Add content to the Special Launch Event tab
# with tab5:
#     with st.expander("See Design Options"):
#         st.markdown(''':red[Special Launch Drinkogniser Design Options]''')
#         design5 = st.select_slider(
#         'Select design options',
#         options=['Design A','Design B','Design C', 'Design D', 'Design E',],key='d5')
#         st.info(f'Your selected {design5}')

# User Interaction
with st.expander(":shopping_trolley: How to Order?"):
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Proceed to Generic Theme Order"):
            st.switch_page("pages/01_Order_Generic_Design.py")
    
    with col2:
        if st.button("Proceed to Customised Theme Order"):
            st.switch_page("pages/02_Order_Customised_Design.py")        
            
    # with st.form("user_info_form"):
    #     # User input fields
    #     name = st.text_input("Specify your name")
    #     email = st.text_input("Enter your email")
    #     design_option = st.radio("Select your Drinkorganiser design options:", 
    #                              ["Wedding", "Birthday", "Kids Party", "Conference", "Special Launch"])
    #     selected_color = st.color_picker("Pick a color for the design", '#0A45E2')
        
    #     # Slider for the number of tags
    #     number_of_tags = st.slider("Number of tags to order", min_value=12, 
    #                                max_value=960, step=12)

    #     # Submit button - it's always visible but will work only if name and email are entered
    #     submitted = st.form_submit_button("Prepare Order")

    #     if submitted and name and email:
    #         user_data = {
    #                     "Name": name,
    #                     "Email": email,
    #                     "Design": design_option,
    #                     "Color": selected_color,
    #                     "Number of Tags": number_of_tags
    #                 }
    #         df = pd.DataFrame([user_data])
    #         st.dataframe(df,hide_index=True)
    #         st.markdown(get_table_download_link(df),unsafe_allow_html=True)
        
    #     elif submitted:
    #         st.error("Please enter your name and email to submit.")



