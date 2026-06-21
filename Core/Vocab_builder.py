

def vocab_build(tokenized):
    vocab = {}
    index = 0
    for token in tokenized:
        if token not in vocab:
            vocab[token] = index
            index += 1
    return vocab        
