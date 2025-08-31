import re


class SimpleTokenizerV1:
  def __init__(self, vocab):
      self.str_to_int = vocab
      self.int_to_str = {integer: token for token, integer in vocab.items()}

  
  def encode(self, text):
      preprocessed = re.split(r'([,.?_!"()\')', text)
      preprocessed = [
          item.strip() for item in preprocessed if item.strip()
      ]
      ids = [self.str_to_int[token] for token in preprocessed]
      return ids

  def decode(self, ids):
      text = " ".join([self.int_to_str[id] for id in ids])
      text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
      return text


if __name__ == "__main__":
    # Reading the input data and creating a vocabulary out of it.
    file_path = "../Data/Chapter-2/the-verdict.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    all_words = sorted(set(preprocessed))
    vocab = {token:integer for integer,token in enumerate(all_words)}

    # Instantitate the Tokenizer
    tokenizer = SimpleTokenizerV1(vocab)

    # Encode the input data
    text = """"It's the last he painted, you know," 
       Mrs. Gisburn said with pardonable pride."""
    ids = tokenizer.encode(text)
    print(ids)

    # Decode the Ids
    print(tokenizer.decode(ids))

    # Encoding that doesn't work
    text = "Hello, do you like tea?"
    print(tokenizer.encode(text)) # throws the KeyError that it cannot find token "hello" in the vocabulary.
