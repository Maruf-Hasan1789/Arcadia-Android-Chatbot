import re


def clean_text(txt):
    txt = txt.lower()
    txt = re.sub(r"i'm", "i am", txt)
    txt = re.sub(r"it's", "it is", txt)
    txt = re.sub(r"he's", "he is", txt)
    txt = re.sub(r"she's", "she is", txt)
    txt = re.sub(r"that's", "that is", txt)
    txt = re.sub(r"what's", "what is", txt)
    txt = re.sub(r"where's", "where is", txt)
    txt = re.sub(r"\'ll", " will", txt)
    txt = re.sub(r"\'ve", " have", txt)
    txt = re.sub(r"\'re", " are", txt)
    txt = re.sub(r"\'d", " would", txt)
    txt = re.sub(r"won't", "will not", txt)
    txt = re.sub(r"can't", "can not", txt)

    return txt


def create_training_data():
    data_path = "human_text.txt"
    data_path2 = "robot_text.txt"
    # Defining lines as a list of each line
    with open(data_path, "r", encoding='utf-8') as f:
        lines = f.read().split('\n')
    with open(data_path2, "r", encoding='utf-8') as f:
        lines2 = f.read().split('\n')
    lines = [re.sub(r"\[\w+\]", 'hi', line) for line in lines]
    lines = [" ".join(re.findall(r"\w+", line)) for line in lines]
    lines2 = [re.sub(r"\[\w+\]", '', line) for line in lines2]
    lines2 = [" ".join(re.findall(r"\w+", line)) for line in lines2]

    encoder_input_data = []
    decoder_input_data = []
    decoder_output_data = []


    for i in range(len(lines)):
        encoder_input_data.append(clean_text(lines[i]))
        decoder_input_data.append('<sos> ' + clean_text(lines2[i]))
        decoder_output_data.append(clean_text(lines2[i]) + ' <eos>')

    print(encoder_input_data[:5])
    return encoder_input_data, decoder_input_data, decoder_output_data


create_training_data()
