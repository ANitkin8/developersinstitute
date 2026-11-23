#exercise 1

import pandas as pd
df = pd.read_csv('train.csv')
duplicate_count = df.duplicated().sum()
print(f"there are {duplicate_count} duplicate rows")
row_count = len(df)
print(f"there are {row_count} rows")
new_df= df.drop_duplicates()
new_row_count = len(new_df)
print(f"there are {new_row_count} new rows")

#exercise 2
from sklearn.impute import SimpleImputer
#make a copy of the data
df_clean = df.copy()
#check which values are missing
missing_counts = new_df.isnull().sum()
print(missing_counts)
#to remove the cabin column
df_clean = df_clean.drop(columns=['Cabin'])
#fill age using median calculated by SimpleImputer
age_imputer = SimpleImputer(strategy='median')
df_clean[["Age"]] = age_imputer.fit_transform(df_clean[["Age"]])
#fill 'Embarked' with "unknown"
df_clean["Embarked"] = df_clean["Embarked"].fillna("Unknown")
#exercise 3
#extract a title from the name column
df_clean["Title"] = df_clean["Name"].str.extract(r",\s*([A-Za-z]+)\.", expand=False).str.strip()
#create a new column of "family size" by adding the SibSp and Parch columns
df_clean["Family_Size"] = df_clean["SibSp"] + df_clean["Parch"] + 1

#exercise 4
import matplotlib.pyplot as plt
import numpy as np
histogram_fare = df_clean["Fare"].hist(bins=20)
plt.show()
histogram_age =df_clean["Age"].hist(bins=20)
plt.show()
#calculating outliers, then creating a new dataset without them
q01 = df_clean.quantile(0.01, numeric_only=True)
q99 = df_clean.quantile(0.99, numeric_only=True)
df_no_outliers = df_clean[(df_clean["Fare"] >= q01["Fare"])
    & (df_clean["Fare"] <= q99["Fare"])
    & (df_clean["Age"] >= q01["Age"])
    & (df_clean["Age"] <= q99["Age"])]
#log transformation
df_log = df_clean.copy()
df_log["Fare_log"] = np.log1p(df_log["Fare"])
new_rows = len(df_no_outliers)
old_rows = len(df_clean)
print(f"there are {new_rows} new rows, down from {old_rows} rows")

#exercise 6
cat_cols = df_clean.select_dtypes(include=["object", "category", "string"]).columns
print("Categorical columns:", list(cat_cols))
df_encoded = pd.get_dummies(df_clean, columns=["Title", "Sex" , "Embarked"], drop_first=False, dtype=int,)

# exercise 5
from sklearn.preprocessing import MinMaxScaler, StandardScaler
df_scaled = df_clean.copy()
scaler_std = StandardScaler()
scaler_mm = MinMaxScaler()
#StandardScaler for Normal
df_scaled["Age_Scaled"] = scaler_std.fit_transform(df_scaled[["Age"]])
#MinMaxScaler for skewed/bounded features
df_scaled["Fare_Scaled"] = scaler_mm.fit_transform(df_scaled[["Fare"]])

#exercise 7
Age_Groups = pd.cut(df_clean["Age"], bins=[0, 12, 18, 60, 100], labels= ["child", "teen", "adult", "senior"], include_lowest=True,)
#create one-hot encoding
age_dummies = pd.get_dummies(Age_Groups)
#to add the new columns back into the dataset
df_clean = pd.concat([df_clean, age_dummies], axis=1)
