
import streamlit as st
import pandas as pd
from streamlit_image_select import image_select
import os

#  pip install streamlit-image-select


# Define the relative path to the directory containing the images


# Function to load images from the specified folder
def load_images_from_folder(folder):
    
    images = []
    
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(folder, filename)
            images.append(img_path)
            
    return images


def list_files(directory):
    
    image_directory = os.path.join(current_directory, directory)
    
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    # List all files in the directory
    image_list = [os.path.relpath(os.path.join(image_directory, f), 
                                  current_directory) 
                  for f in os.listdir(image_directory) 
                  if f.endswith(('.jpg', '.png'))]

    
    # Print the list of image file names
    # for image_name in image_list:
    #     print(image_name)

    return image_list


st.subheader("Custom Design Options")

# header_image = 'data_orig/Anatomy.png'
# st.image(header_image, width=450, caption="Design Anatomy")

# Replace 'data_orig/design_icons' with the actual path if different
dirfront =  os.path.join('pages','data_orig','front_icons')
dirback = os.path.join('pages','data_orig','back_icons')
#front_list = list_files(dirfront)
#back_list = list_files(dirback)
#st.info(front_list)
front_list = load_images_from_folder(dirfront)
st.info(front_list)
# back_list = load_images_from_folder(dirback)


CustomMenu = [
        "Front Options  :arrow_forward:", 
        "Back Options   :arrow_forward:", 
        "Your Guest List  :arrow_forward:", 
        "Your Selection   :arrow_forward:", 
        ":shopping_trolley:  Proceed to Order",
        ]

fd, bd, gl, yl, po = st.tabs(CustomMenu)

with fd:
    st.info("Choose Front Design")

    imgfront = image_select(
        label="Select Your Front Design:",
        images=front_list, use_container_width=False
    
    )

with bd:
    st.info("Choose Back Design")

    
    imgback = image_select(
        label="Select Your Front Design:",
        images=back_list, use_container_width=False
    
    )    
    

with gl:
    
        
    st.info("Specify name/s for each drinognizer tag and separate using Enter key")
    guests = st.text_area( "Paste here:", 
                          value=" Napoleon and Josephine, \n Gary and Linda,"
                          )
    if guests:
        lines = guests.split("\n")
        num_lines = len(lines)
        st.info(f"Qty of tags based on guest list: {num_lines}")   



with yl:
    st.error("Selected Design Options")
    front, back = st.columns(2)
    
    with front:
        st.write("Selected Front Design")
        st.image(imgfront, width=350)
        fselection = str(imgfront)[:100]
        st.write(fselection)

    with back:
        st.write("Selected Back Design")
        st.image(imgback, width=350)
        bselection = str(imgback)[:100]
        st.write(bselection)

    if guests:
        lines = guests.split("\n")
        num_lines = len(lines)
        st.error(f"Qty of tags based on guest list: {num_lines}")        

# User Interaction
with po:
    
    st.info("Complete Your Order")
    
    with st.form("Order Form"):
        # Add input fields to the form
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        
        add_info = st.text_input("Additional Information")
        
        fd1, bd1 = st.columns(2)
        
        with fd1:
            front_image = st.image(imgfront, width=200)
            # front_design = st.write(fselection)
        
        with bd1:
            back_image = st.image(imgback, width=200) 
            # back_design = st.write(bselection)


        quantity = st.number_input("Qty", value=num_lines)
        
        price_per_item = 0.75
        # Calculate the total to pay based on quantity (you can replace this with your own calculation logic)
        total_to_pay = quantity * price_per_item  # Assuming each item costs $10
        

        
        submitted = st.form_submit_button("Submit")
    
        # Process the form data if submitted
    if submitted:
        # You can access the form data here and process it as needed
        
        # Display the total to pay
        st.success("""Your Order submitted Successfully! """)    
        
        st.write(f" Your name: {name}")
        st.write(f" Your email: {email}")
        
        st.write(fselection)
        st.write(bselection)
        
        st.success(f""" Price per item: £{price_per_item:.2f} 
                   Quantity: {quantity} 
                   Total to Pay: £{total_to_pay:.2f}
                   """) 
        
