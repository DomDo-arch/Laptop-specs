import streamlit as st
from streamlit_dynamic_filters import DynamicFilters

import pandas as pd
 
cpu_col, gpu_col = [], []

df = pd.read_csv("laptops_20.csv")

dynamic_filters = DynamicFilters(df = df, filters = ["cpu", "gpu", "ram", "memory"]#, "price_range"])

# Table of column stats
from collections import Counter

cpu_count = pd.DataFrame(dict(Counter(df.cpu)).items())
cpu_count.rename(columns = {0:"cpu",1:"cpu_count"}, inplace = True)

cpu_count = cpu_count.sort_values("cpu_count", ascending = False)

if __name__ == "__main__":

	dynamic_filters.display_filters()
	dynamic_filters.display_df()
	
	#st.write((cpu_count))
