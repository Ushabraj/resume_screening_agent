from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TFIDFEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def compute_similarity(self, query, document):
        vectors = self.vectorizer.fit_transform([query, document])
        sim_matrix = cosine_similarity(vectors)
        return float(sim_matrix[0,1])
