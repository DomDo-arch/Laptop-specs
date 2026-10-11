import streamlit as st
from streamlit_dynamic_filters import DynamicFilters

import pandas as pd

#df = pd.read_csv("laptops_20.csv")

# Table of column stats
laptop_json = st.secrets["laptop_json"]

dynamic_filters = DynamicFilters(df = laptop_json, filters = ["cpu", "gpu", "ram", "memory"])#, "price_range"])

if __name__ == "__main__":

	dynamic_filters.display_filters()
	dynamic_filters.display_df()
	
	#st.write((cpu_count))
