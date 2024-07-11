import streamlit as st
# from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

st.title("Customize your smoothie")
st.write("Choose the fruits")

name = st.text_input("Name of smoothie")
st.write('Name will be', name)

cnx = st.connection("snowflake")
session = cnx.session()
my_df = session.table('smoothies.public.fruit_options').select(col('FRUIT_NAME'))

ings = st.multiselect('Choose up to 5', my_df, max_selections=5)

if ings:
    ingst = ''
    for fc in ings:
        ingst += fc + ' '
    myins = "insert into smoothies.public.orders(ingredients, name_on_order) values('" + ingst + "', '" + name + "')"
    submit = st.button('Submit order')
    if submit:
        session.sql(myins).collect()
        st.success('Smoothie is ordered! ' + name, icon="✔")

import requests
fv_resp = requests.get('https://fruityvice.com/api/fruit/watermelon')
st.text(fv_resp)
