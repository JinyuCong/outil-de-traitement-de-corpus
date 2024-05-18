import pandas as pd
from datasets import Dataset
from sklearn.model_selection import train_test_split

file_path = '../data/dataset.csv'
df = pd.read_csv(file_path)
df = df.iloc[:, :2]

dataset = Dataset.from_pandas(df)

train_df, test_df = train_test_split(dataset, test_size=0.2, random_state=42)

train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)