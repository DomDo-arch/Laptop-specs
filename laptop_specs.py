import streamlit as st
from streamlit_dynamic_filters import DynamicFilters

import pandas as pd

df = pd.read_csv("laptops_20.csv")

dynamic_filters = DynamicFilters(df = df, filters = ["cpu", "gpu", "ram", "memory"])#, "price_range"])

# Table of column stats
st.write(st.secrets["db_password"])
st.write(st.secrets["db_json"])

#df1 = pd.read_json(st.secrets["db_json"])

#st.write(df1)

json = st.secrets["db_json"]
st.write(pd.DataFrame(json.items()))
laptop_json = st.secrets["laptop_json"]
st.write(laptop_json)


if __name__ == "__main__":

	dynamic_filters.display_filters()
	dynamic_filters.display_df()
	
	#st.write((cpu_count))
