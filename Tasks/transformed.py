## Step 3: Transform data
### Import libraries
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.feature_selection import SelectKBest, f_classif
from Tasks.cleaned_and_appended import df

### Encode categorical variables
le = LabelEncoder()
df['protocol_type'] = le.fit_transform(df['protocol_type'])
df['service'] = le.fit_transform(df['service'])
df['flag'] = le.fit_transform(df['flag'])

### Normalize numerical variables
scaler = MinMaxScaler()
num_cols = ['duration', 'src_bytes', 'dst_bytes', 'count', 'srv_count', 'same_srv_rate', 'diff_srv_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_serror_rate']
df[num_cols] = scaler.fit_transform(df[num_cols])

### Feature engineering
# Create a new feature that measures the ratio of source bytes to destination bytes
df['src_dst_ratio'] = df['src_bytes'] / (df['dst_bytes'] + 0.001)

### Feature selection
# Use SelectKBest with ANOVA F-value to select the 10 best features
selector = SelectKBest(f_classif, k=10)
selector.fit(df.drop('attack', axis=1), df['attack'])
selected_cols = df.drop('attack', axis=1).columns[selector.get_support()]
print('The selected features are:', selected_cols)

##########


## Step 4: Split data
# Import libraries
from sklearn.model_selection import train_test_split

### Split the dataset into training and testing sets
'''  
  We use the train_test_split function to split the dataset into 
    features (df.drop('attack', axis=1)) and 
    labels (df['attack']) subsets, 
    with 
      a test size of 0.3 (30% of the data) and 
      a random state of 42 (for reproducibility).
'''
X_train, X_test, y_train, y_test = train_test_split(df.drop('attack', axis=1), df['attack'], test_size=0.3, random_state=42)

### Print the shapes of the subsets
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)