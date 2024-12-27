# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head(5))

# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed, codecademy.score)  # Switched x and y for better visualization
plt.xlabel("Lessons Completed")
plt.ylabel("Score")
plt.title("Score vs. Lessons Completed")
plt.show()
plt.clf()  # Clear the plot

# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula('score ~ completed', data=codecademy)
results = model.fit()
print(results.summary())

# Intercept interpretation:
# the intercept 13.2141 is the minimum score if the student doesn't complete any lesson

# Slope interpretation:
# the completed 1.3068 is the increment of the score for each lesson completed.

# Plot the scatter plot with the regression line
plt.scatter(codecademy.completed, codecademy.score)
plt.xlabel("Lessons Completed")
plt.ylabel("Score")
plt.title("Score vs. Lessons Completed")
predicted_score = results.params[1] * codecademy.completed + results.params[0]
plt.plot(codecademy.completed, predicted_score, color='red', label='Regression Line')  # Switched x and y
plt.legend()
plt.show()
plt.clf()

# Predict score for a learner who has completed 20 prior lessons
predicted_20 = results.params[1] * 20 + results.params[0]
print("Predicted score for a learner with 20 completed lessons:", predicted_20)

# Calculate fitted values and residuals
fitted_values = results.predict(codecademy.completed)
residuals = codecademy.score - fitted_values

# Diagnostic plots
plt.hist(residuals)
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.title("Histogram of Residuals")
plt.show()
plt.clf()

plt.scatter(fitted_values, residuals)
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs. Fitted Values")
plt.show()
plt.clf()

# Create a boxplot of score vs lesson
sns.boxplot(x='lesson', y='score', data=codecademy)  # Specify x and y
plt.xlabel("Lesson")
plt.ylabel("Score")
plt.title("Score vs. Lesson")
plt.show()
plt.clf()

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula('score ~ lesson', data=codecademy)
results = model.fit()
print(results.summary())

# Calculate and print the group means and mean difference
print(codecademy.groupby('lesson').mean().score)
difference = 47.578 - 59.220
print("Mean difference between lessons:", difference)

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x='completed', y='score', hue='lesson', data=codecademy)
plt.xlabel("Lessons Completed")
plt.ylabel("Score")
plt.title("Score vs. Lessons Completed by Lesson")
plt.show()
