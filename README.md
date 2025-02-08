# Project: Artificial Intelligence for the Prescription of a Diet Plan for Cats

## 1. Project Presentation

### Context and Objectives
The diet of cats plays a crucial role in their health and well-being. A veterinarian, when examining a cat, notes its main characteristics:

- **Age**: Helps adapt the diet to the nutritional needs at different growth stages.
- **Weight**: Essential to determine the necessary caloric intake.
- **Activity level**: Influences the amount of energy the cat needs to consume.

Based on this data, a veterinarian prescribes an optimal diet plan including:

- **Daily caloric intake**
- **Meal composition** (type of food and portions)
- **Hydration goal**
- **Specific recommendations**

The goal of our project is to develop an artificial intelligence capable of reproducing this diagnostic and diet prescription process. We have collected and processed a database of nearly 2000 cats, including their characteristics and the diet prescriptions provided by a veterinarian.

Thus, our artificial intelligence model can issue a precise diagnosis based on the data entered by a user regarding their own cat.

## 2. Project Steps

### Data Collection and Processing
1. **Collaboration with a veterinarian**: We obtained a dataset containing the characteristics of 2000 cats as well as their diet prescriptions.
2. **Data structuring**: Each record contains:
    - Age (in years)
    - Weight (in kg)
    - Activity level (low, medium, high)
    - Recommended daily calories
    - Type and amount of food recommended
    - Recommended water intake
    - Specific recommendations from the veterinarian
3. **Data cleaning and preparation**: Removal of outliers, conversion of units, and standardization of data to ensure consistency.

### Modeling with k-Nearest Neighbors (k-NN)

#### Algorithm Choice
We opted for an **unsupervised machine learning** model based on the **k-Nearest Neighbors (k-NN)** algorithm to recommend an optimal diet plan based on the cat's characteristics (age, weight, activity level).

#### Training and Validation
- **Data preprocessing**: Normalization of features (`Age`, `Weight`, `Activity Level`) with `MinMaxScaler` to improve prediction accuracy.
- **Model construction**: Use of `NearestNeighbors(n_neighbors=1, algorithm='ball_tree')` to find the most similar cat in the database.
- **Evaluation**: Recommendations are based on the closest cat in terms of characteristics.

#### Optimization and Adjustments
- **Encoding categorical variables** (activity level) with `LabelEncoder` to ensure better compatibility with the algorithm.
- **Scaling input and output data** to homogenize values and avoid bias due to different measurement scales.
- **Selection of the "ball_tree" algorithm** to optimize the search for the nearest neighbors, particularly suited for small datasets with few dimensions.

### Integration and Testing
7. **Development of a user interface**: We designed an intuitive form allowing users to input their cat's characteristics.
8. **Prediction of the optimal diet plan**: The model analyzes the entered data and returns a personalized meal plan.
9. **Result validation**: Testing with real cases to assess the accuracy of the system.

## 3. Detailed Functioning

### Input Data
- **Age** (in years)
- **Weight** (kg)
- **Activity level** (low, medium, high)

### Data Processing
- Normalization of inputs to match the training data.
- Prediction of the meal plan based on similar cases.
- Generation of a detailed report including the recommended diet and the veterinarian's advice.

### Output Example
For a 3-year-old cat, weighing 4 kg, with moderate activity:

```json
{
  "Daily Calories": 251,
  "Meals": {
      "Breakfast": {
          "Food": "Beef",
          "Portion (g)": 67,
          "Calories": 135
      },
      "Lunch": {
          "Food": "Lamb",
          "Portion (g)": 52,
          "Calories": 117
      },
      "Dinner": {
          "Food": "Beef",
          "Portion (g)": 31,
          "Calories": 86
      }
  },
  "Water Goal (ml)": 440,
  "Recommendation": "This cat requires 251 kcal per day. Suggested meal plan: Breakfast (Beef, 67g, 135 kcal) at 7 AM, Lunch (Lamb, 52g, 117 kcal) at 12 PM, Dinner (Beef, 31g, 86 kcal) at 6 PM. Hydration goal: 440 ml per day."
}
```

## Conclusion
This project combines artificial intelligence and veterinary expertise to provide personalized dietary recommendations for cat owners. By combining a knowledge base validated by professionals and a high-performing machine learning model, we offer a reliable and accessible solution.

Future improvements include integrating new variables (health problems, dietary preferences) and developing a mobile application for a more intuitive use.

## Watch Video
[![Watch ADD video](https://img.shields.io/badge/Watch-ADD%20video-blue?style=for-the-badge&logo=youtube)](https://drive.google.com/file/d/1nJrc1OWS7gL-EfrxzG0oGs5zXcZiNH5C/view?usp=sharing)
