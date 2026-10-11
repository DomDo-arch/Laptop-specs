import streamlit as st
from streamlit_dynamic_filters import DynamicFilters

import pandas as pd

# Table of column stats
laptop_json = st.secrets["laptop_json"]
laptop_json = pd.DataFrame(laptop_json)

dynamic_filters = DynamicFilters(df = laptop_json, filters = ["cpu", "gpu", "ram", "memory", "display"])#, "price_range"])

if __name__ == "__main__":

	dynamic_filters.display_filters()
	dynamic_filters.display_df()
