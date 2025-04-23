# nobel_prize_winners

import pandas as pd
import os

# Sample data on Nobel Prize winners (Year, Category, Laureate)
data = {
    "Year": [2020, 2019, 2018, 2017, 2016],
    "Category": ["Peace", "Literature", "Physics", "Chemistry", "Medicine"],
    "Laureate": ["World Food Programme", "Peter Handke", "Donna Strickland", "Frances Arnold", "Yoshinori Ohsumi"]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to display the data
def display_data():
    print("Nobel Prize Winners:")
    print(df)

# Function to analyze the number of laureates by category
def analyze_categories():
    category_counts = df["Category"].value_counts()
    print("\nNumber of Nobel Prize Winners by Category:")
    print(category_counts)

# Main function
def main():
    print("Welcome to the Nobel Prize Winners Statistics")
    display_data()
    analyze_categories()

    # Save the data to a CSV file
    df.to_csv("nobel_prize_winners.csv", index=False)
    print("\nData saved to 'nobel_prize_winners.csv'.")

# Run the main function
if __name__ == "__main__":
    main()
