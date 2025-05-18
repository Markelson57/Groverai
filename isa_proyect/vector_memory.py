import faiss
import numpy as np

class VectorMemory:
    def __init__(self, dim=512):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.vectors = []
        self.texts = []

    def add(self, vector: np.ndarray, text: str):
        self.index.add(np.array([vector]))
        self.vectors.append(vector)
        self.texts.append(text)

    def search(self, query_vector: np.ndarray, top_k=5):
        D, I = self.index.search(np.array([query_vector]), top_k)
        results = []
        for idx in I[0]:
            if idx < len(self.texts):
                results.append(self.texts[idx])
        return results
