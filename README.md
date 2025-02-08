# Cat Diet Recommendation API

This project provides a Flask-based API that recommends an optimal diet for a cat based on its age, weight, and activity level. The model uses K-Nearest Neighbors (KNN) to find the closest match from a dataset and returns meal recommendations, daily calories, and water intake.

## Features

- Accepts age, weight, and activity level as input.
- Uses a trained KNN model to find the most similar cat in the dataset.
- Returns a JSON response with daily calories, meals (breakfast, lunch, and dinner), water goals, and diet recommendations.
- API is accessible via HTTP POST requests.
- CORS enabled for cross-origin requests.

## Technologies Used

- Flask
- NumPy
- Pandas
- Scikit-learn
- TensorFlow
- JSON

## Installation & Setup

### Prerequisites

Ensure you have Python installed (version 3.7+).

### Clone the Repository

```bash
git clone https://github.com/rayenlakhal/catFeeder
cd catFeeder
```

### Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Running the Flask Server

```bash
python server.py
```

By default, the server runs on `http://0.0.0.0:3000/`.

## API Endpoints

### 1. Serve the Homepage

**Endpoint:** `GET /`

Returns the `index.html` file.

### 2. Predict Diet for a Cat

**Endpoint:** `POST /predict`

**Request Format (JSON):**

```json
{
  "age": 2.5,
  "weight": 4.0,
  "activity_level": "moderate"
}
```

**Response Format (JSON):**

```json
{
  "Daily Calories": 250,
  "Meals": {
    "Breakfast": {
      "Food": "Chicken",
      "Portion (g)": 50,
      "Calories": 100
    },
    "Lunch": {
      "Food": "Fish",
      "Portion (g)": 60,
      "Calories": 120
    },
    "Dinner": {
      "Food": "Dry Cat Food",
      "Portion (g)": 70,
      "Calories": 140
    }
  },
  "Water Goal (ml)": 300,
  "Recommendation": "Ensure your cat stays hydrated and exercises daily."
}
```

## How It Works

1. The user sends a `POST` request with the cat's details.
2. The Flask API processes the request and scales the input data.
3. It finds the nearest match using the trained KNN model.
4. The API returns the best diet recommendation for the cat.

## Deployment

### Running with Docker (Optional)

```bash
docker build -t cat-diet-api .
docker run -p 3000:3000 cat-diet-api
```

### Running on a Cloud Server

You can deploy this API using services like AWS, Heroku, or DigitalOcean.

## Watch Video
[![Watch ADD video](https://img.shields.io/badge/Watch-ADD%20video-blue?style=for-the-badge&logo=youtube)](https://drive.google.com/file/d/1nJrc1OWS7gL-EfrxzG0oGs5zXcZiNH5C/view?usp=sharing)

## Canva Presentation
[![Watch prosentation](https://img.shields.io/badge/Watch-ADD%20video-blue?style=for-the-badge&logo=canva)](https://www.canva.com/design/DAGeeF0uNIs/5A08txIJAFdf4nOP0dv5QA/edit?utm_content=DAGeeF0uNIs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
