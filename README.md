# Analyzing Codecademy Learner Outcomes with Linear Regression

This repository contains Python code that analyzes Codecademy learner data to understand the relationship between lesson completion, lesson type, and learner scores. It uses linear regression with the `statsmodels` library to model these relationships and provides visualizations to aid in understanding the results.

## Data

The code uses a dataset named `codecademy.csv`. This dataset should contain the following columns:

* **completed:** The number of lessons a learner has completed.
* **score:** The learner's score.
* **lesson:** The type of lesson taken (e.g., 'Lesson A', 'Lesson B').

Make sure to replace `'codecademy.csv'` with the actual path to your data file.

## Analysis

The code performs the following analysis:

1. **Exploratory Data Analysis:** Creates a scatter plot to visualize the relationship between the number of lessons completed and learner scores.
2. **Linear Regression:** Fits linear regression models to predict learner scores based on:
    * The number of lessons completed.
    * The type of lesson taken.
3. **Model Evaluation:**  Calculates fitted values and residuals. Creates diagnostic plots (histograms and scatter plots) to check the assumptions of the linear regression models (normality and homoscedasticity).
4. **Prediction:** Predicts the score for a learner who has completed 20 lessons.
5. **Group Comparisons:**  Calculates and compares the average scores for different lesson types using box plots and group means.
6. **Visualization with Seaborn:** Uses the `seaborn` library to create informative visualizations, including a boxplot of scores by lesson type and an `lmplot` to show the relationship between lessons completed and scores, colored by lesson type.

## Usage

1. Make sure you have the necessary libraries installed (`pandas`, `numpy`, `matplotlib`, `seaborn`, and `statsmodels`). You can install them using `pip install pandas numpy matplotlib seaborn statsmodels`.
2. Place your `codecademy.csv` data file in the same directory as the Python script.
3. Run the Python script.

## Output

The code will produce:

* Scatter plots of score vs. lessons completed.
* Summaries of the linear regression results.
* Diagnostic plots to assess the model assumptions.
* A prediction for the score of a learner with 20 completed lessons.
* A boxplot of score vs. lesson type.
* Group means and mean difference between lesson types.
* A plot showing the relationship between lessons completed and score, colored by lesson type.

## Contributing

Feel free to fork this repository and contribute your own improvements or modifications.

## License

This code is released under the MIT License.
