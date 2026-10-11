import streamlit as st
from streamlit_dynamic_filters import DynamicFilters

import pandas as pd

# Table of column stats
laptop_json = st.secrets["phone_json"]
laptop_json = pd.DataFrame(laptop_json)
laptop_json = laptop_json.sort_values("model", ascending=True)

laptop_json["price"] = laptop_json["price"].str.split()#.astype(int)

dynamic_filters = DynamicFilters(df = laptop_json, filters = ["cpu", "gpu", "ram", "memory", "display"])

if __name__ == "__main__":

	dynamic_filters.display_filters()
	#price = st.number_input("Min price", min_value=0, max_value=max(laptop_json["price"]))
	
	#dynamic_filters.display_df()
	
	filtered_df = dynamic_filters.filter_df()
	#df1 = filtered_df[filtered_df["price"]>=price]
	
	st.write(filtered_df)
