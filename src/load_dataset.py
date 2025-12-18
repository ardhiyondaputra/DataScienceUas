df = pd.read_csv("name_gender_dataset.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df["Gender"].value_counts())
