import streamlit

streamlit.title('My parents newly diner')

streamlit.header('Breakfast')
streamlit.header('Oat Meal')
streamlit.header('Cereals')
streamlit.header('coockies')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import Pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
