import streamlit as st
import pandas as pd


options = ['Generic', 'Girls', 'Boys', 'Mixed Gender', 'Pirate', 'Princess', 
           'Dinosaur','Mermaid', 'Safari']

themes = ["Kids Party", "Conference", "Family Party", 
          "Christmas", "Halloween", "Special Launch Event",
          ]

pack_price = 3.99


df = pd.DataFrame(
    [
        {"Theme": "Kids Party", "Add_To_Order": False, "Qty": 12,  "Options":'Generic'},
        {"Theme": "Conference", "Add_To_Order": False, "Qty": 12, "Options":'Generic'},
        {"Theme": "Family Party", "Add_To_Order": False, "Qty": 12,  "Options":'Generic'},
        {"Theme": "Christmas", "Add_To_Order": False, "Qty": 12,  "Options":'Generic'},
        {"Theme": "Halloween", "Add_To_Order": False, "Qty": 12,  "Options":'Generic'},
        {"Theme": "Special Launch Event", "Add_To_Order": False, "Qty": 12,  "Options":'Generic'},
        
    ]
)


edited_df = st.data_editor(
    df,
    column_config={
        "Theme": st.column_config.SelectboxColumn(
            "Specify Your Theme",
            help="Choose your Theme",
            width="medium",
            options=themes,
            required=True,
        ),
        "Qty": st.column_config.NumberColumn(
            "Tag Quantity",
            help="How many items to order (12-1200)?",
            min_value=12,
            max_value=1200,
            step=12,
            default=12,
            format="%d",
        ),
        "Add_To_Order": "Add to Order?",
        "Options": st.column_config.SelectboxColumn(
            "Additional Options",
            help="Theme Specific Design",
            width="medium",
            options=options,
            required=True,
        )
        
        
        
        
    },

    hide_index=True,num_rows="dynamic"
)

if st.button("Display / Refresh Selected Options"):
    your_order = edited_df.loc[edited_df["Add_To_Order"]]
    if not your_order.empty:
        your_order['Price'] = round(your_order['Qty']/12 * pack_price,2)
        st.dataframe(your_order, hide_index=True)
