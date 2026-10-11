import streamlit as st
from streamlit_dynamic_filters import DynamicFilters

import pandas as pd

df = pd.read_csv("laptops_20.csv")

dynamic_filters = DynamicFilters(df = df, filters = ["cpu", "gpu", "ram", "memory"])#, "price_range"])

# Table of column stats
st.write(st.secrets["db_pass"])

if __name__ == "__main__":

	dynamic_filters.display_filters()
	dynamic_filters.display_df()
	
	#st.write((cpu_count))
