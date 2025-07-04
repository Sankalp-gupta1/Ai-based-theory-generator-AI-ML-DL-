# from sklearn.impute import SimpleImputer
# import numpy as np
# data = [[1, 2, np.nan],
#         [4, np.nan, 6],
#         [np.nan, 8, 9]]
# imputer = SimpleImputer(strategy='mean')
# imputed_data = imputer.fit_transform(data)
# print(data)
# print(imputed_data)



# from sklearn.impute import KNNImputer
# import numpy as np
# data = [[1, 2, np.nan],
#         [4, 5, 6],
#         [np.nan,8,9],
#         [10,11,12]
#        ]
# knn_imputer = KNNImputer(n_neighbors=2)
# imputed_data = knn_imputer.fit_transform(data)
# print(data)
# print(imputed_data)



# from sklearn.preprocessing import MinMaxScaler
# import numpy as np
# data=np.array([[10,20],
#                [15,30],
#                [25,45],
#                [30,60]
#               ])
# scaler=MinMaxScaler()
# scaler.fit(data)
# scaled_data=scaler.transform(data)
# print(data)
# print(scaled_data)


from sklearn.feature_extraction.text import CountVectorizer

# Documents list
documents = [
    "Your Service is very very bad",
    "TCS is service based company.",
    "You work in bad service company."
]

# Initialize the CountVectorizer
count_vectorizer = CountVectorizer()

# Fit and transform the documents
count_matrix = count_vectorizer.fit_transform(documents)

# Print the vocabulary
print("Vocabulary:", count_vectorizer.vocabulary_)

# Print the count matrix as array
print(count_matrix.toarray())



