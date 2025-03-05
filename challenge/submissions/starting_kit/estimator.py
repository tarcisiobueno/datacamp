from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import FunctionTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import make_column_transformer

def get_tf_idf_features(X_df):
    tf_idf = TfidfVectorizer(max_features=100)
    X_df_features = tf_idf.fit_transform(X_df['text'].astype(str))
    return X_df_features.toarray() # Convert to dense format 

cols = ['text']

transformer = make_column_transformer(
    (FunctionTransformer(lambda X_df: get_tf_idf_features(X_df)), cols),
)

pipeline = make_pipeline(
    transformer,
    LogisticRegression()
)

def get_estimator():
    return pipeline