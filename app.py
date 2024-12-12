import streamlit as st
from datetime import datetime

# Set the title of the app
st.title("Welcome to Santa's Workshop!")

# Display a welcome message from Santa Claus
st.header("Ho Ho Ho! Merry Christmas!")
st.subheader("Santa Claus welcomes you to his workshop!")

# Add an image of Santa Claus
st.image("https://example.com/santa_claus_image.jpg", caption="Santa Claus")

# Add some festive text
st.write("""
Welcome to Santa's Workshop! Here, you can explore the magic of Christmas, 
see how toys are made, and even send your wish list to Santa himself. 
Enjoy your stay and have a wonderful holiday season!
""")

# Add a text input for the user's name
name = st.text_input("What's your name?")

# Display a personalized greeting if the user enters their name
if name:
    st.write(f"Ho Ho Ho, {name}! Santa is happy to see you!")

# Add a button to send a wish list to Santa
if st.button("Send Wish List to Santa"):
    st.write("Your wish list has been sent to Santa! He will check it twice!")

# Get the current date
current_date = datetime.now()

# Define the date for Christmas
christmas_date = datetime(current_date.year, 12, 25)

# If Christmas has already passed this year, set the date to next year's Christmas
if current_date > christmas_date:
    christmas_date = datetime(current_date.year + 1, 12, 25)

# Calculate the number of days left until Christmas
days_left = (christmas_date - current_date).days

# Display the number of days left
st.header(f"Only {days_left} days left until Christmas!")

# Add a festive footer
st.write("🎄 Happy Holidays from Santa and the Elves! 🎄")
