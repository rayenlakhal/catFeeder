
<!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>1&period; Pr&eacute;sentation du Projet</title>
            <style>

</style>
    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
      mermaid.initialize({ startOnLoad: true });
    </script>
            
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/markdown.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/highlight.css">
<style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe WPC', 'Segoe UI', system-ui, 'Ubuntu', 'Droid Sans', sans-serif;
                font-size: 20px;
                line-height: 1.6;
            }
        </style>
        <style>
.task-list-item {
    list-style-type: none;
}

.task-list-item-checkbox {
    margin-left: -20px;
    vertical-align: middle;
    pointer-events: none;
}
</style>
<style>
:root {
  --color-note: #0969da;
  --color-tip: #1a7f37;
  --color-warning: #9a6700;
  --color-severe: #bc4c00;
  --color-caution: #d1242f;
  --color-important: #8250df;
}

</style>
<style>
@media (prefers-color-scheme: dark) {
  :root {
    --color-note: #2f81f7;
    --color-tip: #3fb950;
    --color-warning: #d29922;
    --color-severe: #db6d28;
    --color-caution: #f85149;
    --color-important: #a371f7;
  }
}

</style>
<style>
.markdown-alert {
  padding: 0.5rem 1rem;
  margin-bottom: 16px;
  color: inherit;
  border-left: .25em solid #888;
}

.markdown-alert>:first-child {
  margin-top: 0
}

.markdown-alert>:last-child {
  margin-bottom: 0
}

.markdown-alert .markdown-alert-title {
  display: flex;
  font-weight: 500;
  align-items: center;
  line-height: 1
}

.markdown-alert .markdown-alert-title .octicon {
  margin-right: 0.5rem;
  display: inline-block;
  overflow: visible !important;
  vertical-align: text-bottom;
  fill: currentColor;
}

.markdown-alert.markdown-alert-note {
  border-left-color: var(--color-note);
}

.markdown-alert.markdown-alert-note .markdown-alert-title {
  color: var(--color-note);
}

.markdown-alert.markdown-alert-important {
  border-left-color: var(--color-important);
}

.markdown-alert.markdown-alert-important .markdown-alert-title {
  color: var(--color-important);
}

.markdown-alert.markdown-alert-warning {
  border-left-color: var(--color-warning);
}

.markdown-alert.markdown-alert-warning .markdown-alert-title {
  color: var(--color-warning);
}

.markdown-alert.markdown-alert-tip {
  border-left-color: var(--color-tip);
}

.markdown-alert.markdown-alert-tip .markdown-alert-title {
  color: var(--color-tip);
}

.markdown-alert.markdown-alert-caution {
  border-left-color: var(--color-caution);
}

.markdown-alert.markdown-alert-caution .markdown-alert-title {
  color: var(--color-caution);
}

</style>
        
</head>
        <body class="vscode-body vscode-light">
          <p><strong>Project: Artificial Intelligence for the Prescription of a Diet Plan for Cats</strong></p>
          <h2 id="1-project-presentation">1. Project Presentation</h2>
          <h3 id="context-and-objectives">Context and Objectives</h3>
          <p>The diet of cats plays a crucial role in their health and well-being. A veterinarian, when examining a cat, notes its main characteristics:</p>
          <ul>
              <li><strong>Age</strong>: Helps adapt the diet to the nutritional needs at different growth stages.</li>
              <li><strong>Weight</strong>: Essential to determine the necessary caloric intake.</li>
              <li><strong>Activity level</strong>: Influences the amount of energy the cat needs to consume.</li>
          </ul>
          <p>Based on this data, a veterinarian prescribes an optimal diet plan including:</p>
          <ul>
              <li><strong>Daily caloric intake</strong></li>
              <li><strong>Meal composition</strong> (type of food and portions)</li>
              <li><strong>Hydration goal</strong></li>
              <li><strong>Specific recommendations</strong></li>
          </ul>
          <p>The goal of our project is to develop an artificial intelligence capable of reproducing this diagnostic and diet prescription process. We have collected and processed a database of nearly 2000 cats, including their characteristics and the diet prescriptions provided by a veterinarian.</p>
          <p>Thus, our artificial intelligence model can issue a precise diagnosis based on the data entered by a user regarding their own cat.</p>
          <h2 id="2-project-steps">2. Project Steps</h2>
          <h3 id="data-collection-and-processing">Data Collection and Processing</h3>
          <ol>
              <li><strong>Collaboration with a veterinarian</strong>: We obtained a dataset containing the characteristics of 2000 cats as well as their diet prescriptions.</li>
              <li><strong>Data structuring</strong>: Each record contains:
                  <ul>
                      <li>Age (in years)</li>
                      <li>Weight (in kg)</li>
                      <li>Activity level (low, medium, high)</li>
                      <li>Recommended daily calories</li>
                      <li>Type and amount of food recommended</li>
                      <li>Recommended water intake</li>
                      <li>Specific recommendations from the veterinarian</li>
                  </ul>
              </li>
              <li><strong>Data cleaning and preparation</strong>: Removal of outliers, conversion of units, and standardization of data to ensure consistency.</li>
          </ol>
          <h3 id="modeling-with-k-nearest-neighbors-k-nn">Modeling with k-Nearest Neighbors (k-NN)</h3>
          <h4 id="algorithm-choice">Algorithm Choice</h4>
          <p>We opted for an <strong>unsupervised machine learning</strong> model based on the <strong>k-Nearest Neighbors (k-NN)</strong> algorithm to recommend an optimal diet plan based on the cat's characteristics (age, weight, activity level).</p>
          <h4 id="training-and-validation">Training and Validation</h4>
          <ul>
              <li><strong>Data preprocessing</strong>: Normalization of features (<code>Age</code>, <code>Weight</code>, <code>Activity Level</code>) with <code>MinMaxScaler</code> to improve prediction accuracy.</li>
              <li><strong>Model construction</strong>: Use of <code>NearestNeighbors(n_neighbors=1, algorithm='ball_tree')</code> to find the most similar cat in the database.</li>
              <li><strong>Evaluation</strong>: Recommendations are based on the closest cat in terms of characteristics.</li>
          </ul>
           <h4 id="optimization-and-adjustments">Optimization and Adjustments</h4>
          <ul>
              <li><strong>Encoding categorical variables</strong> (activity level) with <code>LabelEncoder</code> to ensure better compatibility with the algorithm.</li>
              <li><strong>Scaling input and output data</strong> to homogenize values and avoid bias due to different measurement scales.</li>
              <li><strong>Selection of the "ball_tree" algorithm</strong> to optimize the search for the nearest neighbors, particularly suited for small datasets with few dimensions.</li>
          </ul>
           <h3 id="integration-and-testing">Integration and Testing</h3>
          <ol start="7">
              <li><strong>Development of a user interface</strong>: We designed an intuitive form allowing users to input their cat's characteristics.</li>
              <li><strong>Prediction of the optimal diet plan</strong>: The model analyzes the entered data and returns a personalized meal plan.</li>
              <li><strong>Result validation</strong>: Testing with real cases to assess the accuracy of the system.</li>
          </ol>
          <h2 id="3-detailed-functioning">3. Detailed Functioning</h2>
          <h3 id="input-data">Input Data</h3>
          <ul>
              <li><strong>Age</strong> (in years)</li>
              <li><strong>Weight</strong> (kg)</li>
              <li><strong>Activity level</strong> (low, medium, high)</li>
          </ul>
          <h3 id="data-processing">Data Processing</h3>
          <ul>
              <li>Normalization of inputs to match the training data.</li>
              <li>Prediction of the meal plan based on similar cases.</li>
              <li>Generation of a detailed report including the recommended diet and the veterinarian's advice.</li>
          </ul>
          <h3 id="output-example">Output Example</h3>
          <p>For a 3-year-old cat, weighing 4 kg, with moderate activity:</p>
          <pre><code>{
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
      </code></pre>
           <h3 id="conclusion">Conclusion</h3>
          <p>This project combines artificial intelligence and veterinary expertise to provide personalized dietary recommendations for cat owners. By combining a knowledge base validated by professionals and a 		high-performing machine learning model, we offer a reliable and accessible solution.</p>
          <p>Future improvements include integrating new variables (health problems, dietary preferences) and developing a mobile application for a more intuitive use.</p>
	 <h2> <a href="https://drive.google.com/file/d/1nJrc1OWS7gL-EfrxzG0oGs5zXcZiNH5C/view?usp=sharing">Watch ADD video</a> </h2>
      </body>
      </html>
      
