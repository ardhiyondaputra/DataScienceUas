X = df["Name"]
y = df["Gender"]

tfidf = TfidfVectorizer(
    analyzer="char",
    ngram_range=(2, 4)
)

X_tfidf = tfidf.fit_transform(X)
