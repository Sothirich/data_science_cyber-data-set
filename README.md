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

#### b. Collect data -- [✅]
Collect the data from the identified sources using appropriate methods such as web scraping, APIs, or manual data entry.

#### c. Clean data -- [✅]
Clean the collected data by removing any errors, inconsistencies, or duplicates.

#### d. Transform data -- [✅]
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
> To see more details, please visit [Feature Selection](Documents/1.%20Selected_Features.md)

<hr>
</details>

#### ~~e. Merge data~~
~~Merge multiple datasets into a single dataset if necessary.~~

#### f. Split data -- [✅]
Split the dataset into training and testing sets for model building and evaluation.

<hr>
</details>

# 3. Explore the data [REQUIRED]
<details>
<summary>Details</summary>
<br>
• Perform exploratory data analysis to understand the data, identify patterns and relationships, and generate hypotheses.

<hr>

#### a. Summarize the data -- [✅]
Generate summary statistics and visualizations to get a high-level overview of the data.

#### b. Check for missing or incomplete data -- [✅]
Identify any missing or incomplete data and decide how to handle it (e.g., impute, remove, or ignore).

#### c. Check for outliers -- [✅]
Identify any outliers in the data and decide how to handle them (e.g., remove, transform, or keep).

#### d. Check for correlations -- [✅]
Calculate correlation coefficients between pairs of variables to identify any relationships.

#### e. Visualize the data -- [✅]
Create visualizations such as scatter plots, histograms, and box plots to explore the distribution of the data and identify patterns and relationships.

#### f. ~~Generate hypotheses~~
~~Based on the exploratory analysis, generate hypotheses about the relationships between variables and their potential impact on the outcome.~~

<hr>
</details>

# 4. Build models [REQUIRED]
<details>
<summary>Details</summary>
<br>
• Select appropriate modeling techniques and build predictive or descriptive models using the prepared data.

<hr>

#### a. Select modeling techniques -- [✅]
Choose appropriate modeling techniques based on the problem, goals, and data of the project.
> To see more details, please visit [Model Selection](Documents/2.%20Selected_Modeling_Techniques.md)

#### ~~b. Preprocess data~~
~~Preprocess the data to prepare it for modeling, such as scaling or normalizing the features.~~

#### c. Train models -- IN PROGRESS
<details>
<summary>Steps</summary>
<br>
• Train the selected models using the preprocessed training data.

<hr>

#### a. Choose a loss function
• A loss function is a measure of how well a model fits the data, and it is used to evaluate and optimize the model during training. 
• A loss function quantifies the difference between the actual and predicted values, and it is usually minimized by adjusting the model parameters and weights. 
> There are different types of loss functions, such as mean squared error, cross-entropy, or hinge loss, and the choice of loss function depends on the type and objective of the model.
> To see more details, please visit [Loss Function](Documents/2.1%20Selected_Loss_Function.md)

#### b. Choose an optimization algorithm
• An optimization algorithm is a method of finding the optimal values of the model parameters and weights that minimize the loss function. 
> There are different types of optimization algorithms, such as gradient descent, stochastic gradient descent, or Adam, and they differ in how they update the model parameters and weights based on the gradient of the loss function.
> To see more details, please visit [Optimization Algorithm](Documents/2.2%20Selected_Optimization_Algorithm.md)

#### c. Choose a learning rate
• A learning rate is a hyperparameter that controls how much the model parameters and weights change in each iteration of the optimization algorithm. 
• A learning rate can affect the speed and accuracy of the model training. 
> A too high learning rate can cause the model to overshoot the optimal values and diverge, while a too low learning rate can cause the model to converge too slowly or get stuck in a local minimum.
> To see more details, please visit [Learning Rate](Documents/2.3%20Selected_Learning_Rate.md)

#### d. Choose a regularization technique
• A regularization technique is a method of preventing overfitting or underfitting of the model by adding a penalty term to the loss function. 
• Overfitting occurs when the model fits the training data too well but performs poorly on new or unseen data, while underfitting occurs when the model fails to capture the complexity or patterns in the data.
> There are different types of regularization techniques, such as L1 or L2 regularization, dropout, or early stopping, and they differ in how they reduce the complexity or variance of the model.
> To see more details, please visit [Regularization Technique](Documents/2.4%20Selected_Regularization_Technique.md)

#### e. Choose a validation strategy
• A validation strategy is a method of evaluating the performance and generalization ability of the model on new or unseen data. 
• A validation strategy can help to select the best model among different candidates or tune the hyperparameters of the model. 
> There are different types of validation strategies, such as hold-out validation, k-fold cross-validation, or leave-one-out cross-validation, and they differ in how they split the data into training, validation, and testing sets.
> To see more details, please visit [Validation Strategy](Documents/2.5%20Selected_Validation_Strategy.md)

<hr>
</details>

#### d. Tune models -- IN PROGRESS
Tune the hyperparameters of the models to optimize their performance.

#### e. Ensemble models -- IN PROGRESS [OPTIONAL]
Combine multiple models into an ensemble model to improve performance and robustness.

<hr>
</details>

# 5. Evaluate models [REQUIRED]
<details>
<summary>Details</summary>
<br>
• Evaluate the performance of the models using appropriate metrics and select the best model for deployment.

<hr>

#### a. Select evaluation metrics -- [✅]
Choose appropriate evaluation metrics based on the problem, goals, and data of the project.
> To see more details, please visit [Evaluation Metrics](Documents/3.%20Selected_Evaluation_Matric.md)

#### b. Test models -- IN PROGRESS
Test the performance of the models using the testing data and the selected evaluation metrics.

#### c. Compare models -- IN PROGRESS
Compare the performance of different models to identify the best model.
> To see more details, please visit [Model Comparison](Documents/0.2%20Assigned_Models_To_Person.md)

#### d. Validate models -- IN PROGRESS
Validate the performance of the selected model using additional data or cross-validation techniques.

#### e. Interpret models -- IN PROGRESS
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
