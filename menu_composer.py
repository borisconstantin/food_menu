from foods_categorized import *
import random
import pandas as pd
import streamlit as st
import time

week_days = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

st.set_page_config(page_title="week foods", layout="wide")

st.title('Home weekly menu generator')

generate = st.button('Generate this week menu')

if generate : 
    with st.spinner('Generating menu...') : 
        time.sleep(5)
        week_breaksfasts = {}
        week_lunchs = {}
        week_dinners = {}

        menu = {}

        for day in week_days : 

            accompanying_bf = random.choice(list(breakfast.keys()))
            accompanying_lc = random.choice(list(lunch.keys()))
            accompanying_dn = random.choice(list(dinner.keys()))

            menu[day] = {'ptit dej' : f'{accompanying_bf} + {random.choice(breakfast[accompanying_bf])}',
                        'Dejeuner' : f'{accompanying_lc} + {random.choice(lunch[accompanying_lc])}',
                        'Dîner' : f'{accompanying_dn} + {random.choice(dinner[accompanying_dn])}'}

        df = pd.DataFrame(menu).T

        st.dataframe(df)
