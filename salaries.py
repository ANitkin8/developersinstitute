import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA

scaler_mm = MinMaxScaler()
df = pd.read_csv("datascience_salaries.csv")
df["salary_scaled"] = scaler_mm.fit_transform(df[["salary"]])
#convert the text columns
X = pd.get_dummies(df.drop(columns=["salary", "salary_scaled"], errors="ignore"), drop_first=False, dtype=int,)
#standardize
scaler_std = StandardScaler()
X_scaled = scaler_std.fit_transform(X)
#reduce to principle components with PCA
pca = PCA(n_components=2)
x_pca = pca.fit_transform(X_scaled)
df["PC1"] = x_pca[:, 0]
df["PC2"] = x_pca[:, 1]
#calculate mean and median
result = df.groupby("experience_level")["salary"].agg(["mean","median"])
print(result)