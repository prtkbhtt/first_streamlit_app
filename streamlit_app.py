
import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My first webpage")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#Create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
       streamlit.error("Please select a fruit to get info.")
  else:
      #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
      #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()




#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

#my_cur = my_cnx.cursor()
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
#my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
#my_data_row = my_cur.fetchall()

streamlit.header("The fruit load list contains:")
def get_fruit_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
         return my_cur.fetchall()
      
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_list()
    streamlit.dataframe(my_data_rows)
      
streamlit.stop()      
#streamlit.dataframe(my_data_row)

fruit_ads = streamlit.text_input('what fruit would like to add?','jackfruit')
fruit_add_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_ads)
streamlit.write('Thanks for adding' , fruit_ads)

