import streamlit as st
from datetime import datetime

# Set the title of the app
st.title("Countdown to Christmas!")

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

# Add some festive text
st.write("""
Get ready for the most wonderful time of the year! 
Make sure to prepare your wish list and be on your best behavior, 
because Santa Claus is coming to town!
""")

# Add a festive footer
st.write("🎄 Happy Holidays! 🎄")
