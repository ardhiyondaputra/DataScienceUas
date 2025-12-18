# lowercase nama
df["Name"] = df["Name"].str.lower()

# hapus duplikasi exact (opsional)
df = df.drop_duplicates(subset=["Name", "Gender"])
