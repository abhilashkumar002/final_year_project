
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
'''
def unit_test_limitizing_word():
	stop_rem_query = input()
	pos = []
	pos = limitizing_word(stop_rem_query)
	print(pos)
'''
query_file = "query.txt"
with open(query_file,'r') as f:
	text = f.read()
	f.close()
#pos = limitizing_word(text)
#print(text)

verb_pos_tags = ['VB','VBD','VBG', 'VBN', 'VBP', 'VBZ']

pos = pos_tag(word_tokenize(text))
l = len(pos)
lemmatizer = WordNetLemmatizer()
#print(lemmatizer.lemmatize('playing','v'))

f = open('query_upgrade.txt','w')

for i in range(l):
	pos[i] = list(pos[i])
	if pos[i][1] in verb_pos_tags:
		pos[i][1] = 'v'
	elif pos[i][0].endswith('ing'):
		pos[i][1] = 'v'
	else:
		pos[i][1] = 'n'
	pos[i][0] = lemmatizer.lemmatize(pos[i][0], pos[i][1])
	f.write(pos[i][0])
	f.write(' ')
f.close()
#print(pos)
