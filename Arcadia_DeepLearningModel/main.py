
from tokenizers import Tokenizer
from generate_response import Predict, Seq2SeqModel



tokenizer = Tokenizer()

# loading tokenizer
tokenizer.load_tokenizer('tokenizer-vocab_size-5000.pickle')

# loading pretrained weight
Seq2SeqModel.load_weights('seq2seq-weights-800-epochs-0.01-learning_rate.h5')

predict = Predict(Seq2SeqModel, tokenizer)

def chatwithbot(text):
    return (predict.create_response(text))




