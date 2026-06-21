# Word-Level tokenizer


def tokenizer(data):
    lower_case_txt = data.lower()
    punctuation = str.maketrans("", "", ",.!?")
    clean_txt = lower_case_txt.translate(punctuation)
    tokens = clean_txt.split()
    
    return tokens
