import tensorflow as tf
import numpy as np
import pandas as pd
import json
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.neighbors import NearestNeighbors

# Load and preprocess the data
with open('cat_diet_data.json') as f:
    data = json.load(f)

# Extract input and output data from the JSON
input_data = []
output_data = []
recommendations = []  # Store the recommendations separately

for cat in data:
    age = cat["Age"]
    weight = cat["Weight"]
    activity_level = cat["Activity Level"]
    
    # Encoding activity level (high, low, moderate)
    activity_encoder = LabelEncoder()
    activity_level_encoded = activity_encoder.fit_transform([activity_level])[0]

    # Collect inputs (Age, Weight, Activity Level)
    input_data.append([age, weight, activity_level_encoded])
    
    # Collect outputs (Daily Calories, Meals, Water Goal, and Recommendation)
    daily_calories = cat["Daily Calories"]
    meals = cat["Meals"]
    water_goal = cat["Water Goal (ml)"]
    recommendation = cat["Recommendation"]
    
    # Meals are converted into separate features for each meal
    breakfast_calories = meals["Breakfast"]["Calories"]
    lunch_calories = meals["Lunch"]["Calories"]
    dinner_calories = meals["Dinner"]["Calories"]
    
    output_data.append([daily_calories, breakfast_calories, lunch_calories, dinner_calories, water_goal])
    recommendations.append(recommendation)  # Store the recommendations separately

# Convert input and output data to numpy arrays
input_data = np.array(input_data)
output_data = np.array(output_data)

# Preprocessing and scaling the data
scaler = MinMaxScaler()
input_data_scaled = scaler.fit_transform(input_data)

output_scaler = MinMaxScaler()
output_data_scaled = output_scaler.fit_transform(output_data)

# Step 2: Create KNN model for nearest neighbors search
knn = NearestNeighbors(n_neighbors=1, algorithm='ball_tree')
knn.fit(input_data_scaled)

# Step 3: Accept user input for new cat

def get_user_input():
    print("Enter the details for the cat:")
    age = float(input("Age (in years): "))
    weight = float(input("Weight (in kg): "))
    
    activity_level = input("Activity Level (high/low/moderate): ").lower()
    
    if activity_level not in ['high', 'low', 'moderate']:
        print("Invalid activity level! Please enter 'high', 'low', or 'moderate'.")
        return None
    
    # Convert activity level to numeric representation
    activity_level_encoded = 0 if activity_level == 'low' else 1 if activity_level == 'moderate' else 2
    return np.array([[age, weight, activity_level_encoded]])

def find_nearest_cat(user_input):
    # Scale the user input
    user_input_scaled = scaler.transform(user_input)
    
    # Find the nearest neighbor
    distances, indices = knn.kneighbors(user_input_scaled)
    
    # Get the nearest cat's output and the recommendation
    nearest_cat = data[indices[0][0]]  # Retrieve full cat details from original JSON data
    
    # Construct the JSON response
    nearest_cat_json = {
        "Daily Calories": nearest_cat["Daily Calories"],
        "Meals": {
            "Breakfast": {
                "Food": nearest_cat["Meals"]["Breakfast"]["Food"],
                "Portion (g)": nearest_cat["Meals"]["Breakfast"]["Portion (g)"],
                "Calories": nearest_cat["Meals"]["Breakfast"]["Calories"]
            },
            "Lunch": {
                "Food": nearest_cat["Meals"]["Lunch"]["Food"],
                "Portion (g)": nearest_cat["Meals"]["Lunch"]["Portion (g)"],
                "Calories": nearest_cat["Meals"]["Lunch"]["Calories"]
            },
            "Dinner": {
                "Food": nearest_cat["Meals"]["Dinner"]["Food"],
                "Portion (g)": nearest_cat["Meals"]["Dinner"]["Portion (g)"],
                "Calories": nearest_cat["Meals"]["Dinner"]["Calories"]
            }
        },
        "Water Goal (ml)": nearest_cat["Water Goal (ml)"],
        "Recommendation": nearest_cat["Recommendation"]
    }
    
    # Save the JSON output to a file
    # with open("nearest_cat.json", "w") as json_file:
    #     json.dump(nearest_cat_json, json_file, indent=4)
    
    # print("Nearest cat details saved to 'nearest_cat.json'.")
    
    # Return the dictionary as a JSON object
    return json.dumps(nearest_cat_json, indent=4)


# Example usage:
# user_input = ...
# print(find_nearest_cat(user_input))


# Get user input
# user_input = get_user_input()

# if user_input is not None:
#     predicted = find_nearest_cat(user_input)
#     print(predicted)