## Step 3: Transform data
### Import libraries
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.feature_selection import SelectKBest, f_classif
import pandas as pd
from cleaned_and_appended import df

### Encode categorical variables
le = LabelEncoder()
df['protocol_type'] = le.fit_transform(df['protocol_type'])
df['service'] = le.fit_transform(df['service'])
df['flag'] = le.fit_transform(df['flag'])

### Normalize numerical variables
scaler = MinMaxScaler()
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
num_cols = num_cols.drop('attack')
df[num_cols] = scaler.fit_transform(df[num_cols])

### Feature engineering
# Create a new feature that measures the ratio of source bytes to destination bytes
df['src_dst_ratio'] = df['src_bytes'] / (df['dst_bytes'] + 0.001)

### Feature selection
# Use SelectKBest with ANOVA F-value to select the 10 best features
selector = SelectKBest(f_classif, k=10)
selector.fit(df.drop('attack', axis=1), df['attack'])
selected_cols = df.drop('attack', axis=1).columns[selector.get_support()]

### Convertion to list
selected_cols = selected_cols.tolist()

### Adding more features to the list
selected_cols.append('duration')
selected_cols.append('dst_bytes')

print('The selected features are:', selected_cols)

##########


## Step 4: Split data
# Import libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

### Define the selected features
selected_features = selected_cols

### Split the dataset into X and y, using the selected features and the attack column
X = df[selected_features]
y = df['attack']

### Split the dataset into training and testing sets, using 70% for training and 30% for testing, and a random state of 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#### Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Print the shapes of the training and testing sets
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)