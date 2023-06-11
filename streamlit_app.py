import streamlit as st
import pymongo
import pandas as pd

# Replace <connection_string> with your actual MongoDB Atlas connection string
client = pymongo.MongoClient("mongodb+srv://kleine:pJdXUtF0X7xNZ7Un@cluster0.g1l9kvw.mongodb.net/?retryWrites=true&w=majority")

# Replace <database_name> and <collection_name> with your actual database and collection names
db = client.db01
collection = db.collection01

# Replace {} with your query filter or aggregation pipeline
query = {}

# Retrieve the data from MongoDB Atlas
cursor = collection.find(query)

# Convert the cursor to a list of dictionaries
data = list(cursor)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Drop the "_id" column
df = df.drop("_id", axis=1)

# Create a Streamlit app
st.title("Sample Data from MongoDB Atlas")

# Display the sample data
st.dataframe(df)

manufacturer_counts = df["Manufacturer"].value_counts()

def main():
    st.title("Manufacturer Distribution")
    st.bar_chart(manufacturer_counts)

if __name__ == "__main__":
    main()

