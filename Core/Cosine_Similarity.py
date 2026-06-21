import math


def cosine_similarity(vector_a, vector_b):
    dot_product = 0
    magnitude_a_squared = 0
    magnitude_b_squared = 0
    
    for i in range(len(vector_a)):
        dot_product += vector_a[i] * vector_b[i]
        magnitude_a_squared += vector_a[i] ** 2
        magnitude_b_squared += vector_b[i] ** 2
        
    if magnitude_a_squared == 0 or magnitude_b_squared == 0:
        return 0.0
        
    similarity = dot_product / (math.sqrt(magnitude_a_squared) * math.sqrt(magnitude_b_squared))
    return similarity

    