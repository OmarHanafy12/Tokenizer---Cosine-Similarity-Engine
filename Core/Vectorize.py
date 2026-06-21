
def Vectorize(Tokenized, Vocab):
    Zeros = [0] * len(Vocab)
    for zero in range(0, len(Vocab)-1):
        Zeros[zero] = 0
    for word in Tokenized:
        if word in Vocab:
            word_index = Vocab[word]
            Zeros[word_index] += 1
    return Zeros

    