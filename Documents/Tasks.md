# 1. Define the problem [REQUIRED]
<details>
  <summary>Details</summary>
  <br>
  • Clearly define the problem you want to solve and the goals you want to achieve.

  <hr>

  #### The goals are to use binomial or multinomial classification techniques to predict whether a network activity is normal or an attack, and if it is an attack, what type of attack it is.

  <hr>
  
</details>



# 2. Collect and prepare data [REQUIRED]
<details>
<summary>Details</summary>
<br>
• Collect relevant data from various sources and clean, preprocess, and transform it into a suitable format for analysis.

<hr>

#### ~~a. Identify data sources~~
~~Identify the sources of data that are relevant to the problem and goals of the project.~~

#### b. Collect data -- DONE
Collect the data from the identified sources using appropriate methods such as web scraping, APIs, or manual data entry.

#### c. Clean data -- DONE
Clean the collected data by removing any errors, inconsistencies, or duplicates.

#### d. Transform data -- DONE
<details>
<summary>Steps</summary>
<br>
• Transform the data into a suitable format for analysis by performing operations such as normalization, encoding, or aggregation.

<hr>

##### I. Encoding categorical variables
Encode categorical variables using techniques such as one-hot encoding or label encoding to convert them into numerical values that can be used in modeling.

##### II. Normalizing numerical variables
Normalize numerical variables to ensure that they have similar scales and ranges, which can improve the performance of some modeling techniques.

##### III. Feature engineering
Create new features by combining or transforming existing features to capture additional information or relationships in the data.

##### IV. Feature selection
Select a subset of the most relevant features to use in modeling, which can improve model performance and interpretability.

<hr>
</details>

#### ~~e. Merge data~~
~~Merge multiple datasets into a single dataset if necessary.~~

#### f. Split data -- DONE
Split the dataset into training and testing sets for model building and evaluation.

<hr>
</details>

# 3. Explore the data [REQUIRED]
<details>
<summary>Details</summary>
<br>
• Perform exploratory data analysis to understand the data, identify patterns and relationships, and generate hypotheses.

<hr>

#### a. Summarize the data -- IN PROGRESS
Generate summary statistics and visualizations to get a high-level overview of the data.

#### b. Check for missing or incomplete data -- IN PROGRESS
Identify any missing or incomplete data and decide how to handle it (e.g., impute, remove, or ignore).

#### c. Check for outliers -- IN PROGRESS
Identify any outliers in the data and decide how to handle them (e.g., remove, transform, or keep).

#### d. Check for correlations -- IN PROGRESS
Calculate correlation coefficients between pairs of variables to identify any relationships.

#### e. Visualize the data -- IN PROGRESS
Create visualizations such as scatter plots, histograms, and box plots to explore the distribution of the data and identify patterns and relationships.

#### f. Generate hypotheses -- IN PROGRESS
Based on the exploratory analysis, generate hypotheses about the relationships between variables and their potential impact on the outcome.

<hr>
</details>

# 4. Build models [REQUIRED]
<details>
<summary>Details</summary>
<br>
• Select appropriate modeling techniques and build predictive or descriptive models using the prepared data.

<hr>

#### a. Select modeling techniques -- IN PROGRESS
Choose appropriate modeling techniques based on the problem, goals, and data of the project.

#### b. Preprocess data -- IN PROGRESS
Preprocess the data to prepare it for modeling, such as scaling or normalizing the features.

#### c. Train models -- IN PROGRESS
Train the selected models using the preprocessed training data.

#### d. Tune models -- IN PROGRESS
Tune the hyperparameters of the models to optimize their performance.

#### e. Ensemble models -- IN PROGRESS
Combine multiple models into an ensemble model to improve performance and robustness.

<hr>
</details>

# 5. Evaluate models [OPTIONAL]
<details>
<summary>Details</summary>
<br>
• Evaluate the performance of the models using appropriate metrics and select the best model for deployment.

<hr>

#### a. Select evaluation metrics
Choose appropriate evaluation metrics based on the problem, goals, and data of the project.

#### b. Test models
Test the performance of the models using the testing data and the selected evaluation metrics.

#### c. Compare models
Compare the performance of different models to identify the best model.

#### d. Validate models
Validate the performance of the selected model using additional data or cross-validation techniques.

#### e. Interpret models
Interpret the results of the model to understand its strengths and weaknesses and to gain insights into the data.

<hr>
</details>

# 6. Deploy models [NOT NECESSARY]
<details>
<summary>Details</summary>
<br>
• Deploy the selected model in a production environment and integrate it with other systems.
</details>

# 7. Monitor and maintain models [NOT NECESSARY]
<details>
<summary>Details</summary>
<br>
• Monitor the performance of the deployed model over time and update or retrain it as needed.
</details>
