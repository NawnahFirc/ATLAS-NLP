"""A trainable word + character TF-IDF support-intent baseline."""

from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import FeatureUnion, Pipeline


def build_baseline(seed: int = 42) -> Any:
    return Pipeline(
        [
            (
                "features",
                FeatureUnion(
                    [
                        ("word", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_features=25000, sublinear_tf=True)),
                        ("char", TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), min_df=2, max_features=35000, sublinear_tf=True)),
                    ]
                ),
            ),
            ("classifier", LogisticRegression(C=4.0, max_iter=300, tol=0.001, random_state=seed)),
        ]
    )
