#Predicting Missing Words in a sentence
import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
logging.basicConfig(level=logging.INFO)

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

#text = '[CLS] The Moon\'s orbit around [MASK] has a sidereal period of 27.3 days. [SEP]'
#text="[CLS] A medium [MASK] provides almost 9% of a person’s daily potassium according to the nutritional information from the above sources.[SEP]"
#text=" The [MASK] producer, or simply the producer, is likened to a film director.[1][3] The executive producer, on the other hand, enables the recording project through entrepreneurship, and an audio engineer operates the technology."
text="The modern automobile is a complex technical system employing subsystems with specific design functions. Some of these consist of thousands of component parts that have evolved from breakthroughs [MASK] existing technology or from new technologies such as electronic computers, high-strength plastics, and new alloys of steel and nonferrous metals. Some subsystems have come about as a result of factors such as air pollution, safety legislation, and competition between manufacturers throughout the world."
text="[CLS] " +text +" [SEP]"
print (text)
tokenized_text = tokenizer.tokenize(text)
#print (tokenized_text)
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
#print(indexed_tokens)
# Create the segments tensors.
segments_ids = [0] * len(tokenized_text)
print (segments_ids)
# Convert inputs to PyTorch tensors
tokens_tensor = torch.tensor([indexed_tokens])
print (tokens_tensor)

segments_tensors = torch.tensor([segments_ids])

# Load pre-trained model (weights)
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
model.eval()

# Predict all tokens
with torch.no_grad():
    predictions = model(tokens_tensor, segments_tensors)
masked_index = tokenized_text.index('[MASK]')
predicted_index = torch.argmax(predictions[0, masked_index]).item()
predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]

print(predicted_token)