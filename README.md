# Tokenizer & Cosine Similarity Engine

A lightweight, from-scratch natural language processing (NLP) pipeline and vector similarity engine implemented entirely in pure Python. This project completely avoids external machine learning frameworks or numerical computing libraries (such as NumPy, scikit-learn, or NLTK) to demonstrate the core mathematical and algorithmic foundations of tokenization, vocabulary indexing, spatial vectorization, and coordinate geometry.

## 🚀 Architectural Overview

The engine processes raw unstructured text through a modular, four-stage deterministic data pipeline to calculate spatial distance between documents:

```text
[Raw Text String] ──> (Tokenizer) ──> [Clean Token Arrays]
                                             │
                                             ▼
[Numerical Spatial Vectors] <── (Vectorizer) <── [Shared Vocabulary Map]
              │
              ▼
    (Similarity Engine) ──> [Cosine Metric: 0.0 to 1.0]