from Core import Cosine_Similarity, Tokenizer, Vectorize, Vocab_builder

with open("Tokenizer & Cosine Similarity Engine/Data/test_a.txt" , 'r') as file:
    data_a = file.read().replace('\n', ' ')
with open("Tokenizer & Cosine Similarity Engine/Data/test_b.txt" , 'r') as file:
    data_b = file.read().replace('\n', ' ')
with open("Tokenizer & Cosine Similarity Engine/Data/test_c.txt" , 'r') as file:
    data_c = file.read().replace('\n', ' ')


token_a = Tokenizer.tokenizer(data_a)
token_b = Tokenizer.tokenizer(data_b)
token_c = Tokenizer.tokenizer(data_c)

dictionary  = Vocab_builder.vocab_build(token_a + token_b + token_c)

vector_a = Vectorize.Vectorize(token_a, dictionary)
vector_b = Vectorize.Vectorize(token_b, dictionary)
vector_c = Vectorize.Vectorize(token_c, dictionary)

test_1 = Cosine_Similarity.cosine_similarity(vector_a, vector_b)
test_2 = Cosine_Similarity.cosine_similarity(vector_b,vector_c)

print(test_1, test_2)



