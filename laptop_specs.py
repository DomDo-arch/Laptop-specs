import streamlit as st
from streamlit_dynamic_filters import DynamicFilters

import pandas as pd

device = st.segmented_control("Device", ["Phone", "Laptop"], default = "Phone")

# Table of column stats
if device == "Phone":
	laptop_json = st.secrets["phone_json"]
else:
	laptop_json = st.secrets["laptop_json"]

laptop_json = pd.DataFrame(laptop_json)
laptop_json = laptop_json.sort_values("model", ascending=True)

laptop_json["price"] = [int(x[0].replace("$","")) for x in laptop_json["price"].str.split("-")]#.astype(int)

dynamic_filters = DynamicFilters(df = laptop_json, filters = ["cpu", "gpu", "ram", "memory", "display"])

if __name__ == "__main__":
	filtered_df = dynamic_filters.filter_df()
	
	dynamic_filters.display_filters(num_columns = 2, gap = "large", location = "columns")
	price = st.number_input("Min price", min_value=0, max_value=max(laptop_json["price"]))
	
	if device == "Phone":
		battery = st.number_input("Select battery", min_value=0, max_value=max(laptop_json["battery(mAh)"].astype(int)))
		df1 = filtered_df[filtered_df["price"]>=price]
		df1 = df1[(df1["battery(mAh)"]).astype(int)>=battery]
	else:
		st.write(float(max(laptop_json["battery(Wh)"])))
		battery = st.number_input("Select battery", min_value=0, max_value=100)#max(laptop_json["battery(Wh)"].astype(float)))
		df1 = filtered_df[filtered_df["price"]>=price]
		df1 = df1[(df1["battery(Wh)"]).astype(float)>=battery]
	
	#dynamic_filters.display_df()
	
	st.write(df1)
