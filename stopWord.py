from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open('query.txt', 'r') as f:
    query = f.read()
    f.close()
query = query.lower()

stop_words = set(stopwords.words('english'))
stop_words.remove('out')
stop_words.update(',', '"', "'", '-', '&','?','!')
#print(stop_words)
word_tokens = word_tokenize(query)
 
filtered_query = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_query.append(w)

with open('query.txt', 'w') as f:
    f.write('')
    f.close()

with open('query.txt','a') as f:
    for i in filtered_query:
        f.write(i + ' ')
    f.close()