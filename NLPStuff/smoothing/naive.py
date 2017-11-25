import re,operator
import sys
import math
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *
from collections import defaultdict

files=["news.txt","anime.txt","movies.txt"]
all_unigram={}	
for file in files:
	f = open(file)
	unigram_dict=defaultdict(int)
	unigram=re.sub('http[s]? : //(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',' ', f.read())
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ', unigram)
	unigram=re.sub('(\.)+','.', unigram)
	tokens=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|\.|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
	#tokens=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|,|&|2}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',f.read())
	unigram_dict={}
	for k in tokens:
		try:
			unigram_dict[k]+=1
		except:
			unigram_dict[k]=1
	all_unigram[file]=unigram_dict		

def merge_unigrams(unigrams):
	all_words = set([word for author in unigrams for word in unigrams[author]])
	for word in all_words:
		for author in unigrams:
			if word not in unigrams[author]:
				unigrams[author][word] = 0
	print("Total unique words", len(all_words))
	return all_words
all_words = merge_unigrams(all_unigram)

def convert_to_probs(all_unigrams):
	uprobs = {}
	for author in all_unigrams:
		V = len(list(all_unigrams[author].keys()))
		N = sum(list(all_unigrams[author].values()))
		uprobs[author] = {}
		for word in all_unigrams[author]:
			#uprobs[author][word] = unigrams[author][word] / float(N)
			uprobs[author][word] = (all_unigrams[author][word] + 1)/ (float(N) + V)
	return uprobs

uprobs=convert_to_probs(all_unigram)




all_words = merge_unigrams(all_unigram)
utable = [(word, [all_unigram[author][word] for author in all_unigram]) for word in all_words]
sorted_utable = sorted(utable, key = lambda x: sum(x[1]), reverse=True)
sorted_utable = sorted_utable[:500]
authors = list(all_unigram.keys())
get_v_for_auth = lambda x : list(zip(*list(zip(*sorted_utable))[1]))[authors.index(x)]
plot([Bar({"x" : list(zip(*sorted_utable))[0], "y": get_v_for_auth(author)}, name=author) for author in all_unigram],filename="test1")

def sentence_prob(sentence):
	probs = []
	for author in uprobs:
		p = 1.0
		for word in sentence:
			print word
			p *= uprobs[author][word]
			probs += [(author, p)]
	return probs


sentence = 'this is a bright day'.split(' ')
sprobs = sentence_prob(sentence)
print(sprobs)
plot([ Bar({"x" : list(zip(*sprobs))[0], "y": list(zip(*sprobs))[1]})],filename="test4")
plot([ Bar({"x" : sentence, "y": [uprobs[author][w] for w in sentence]}, name=author) for author in all_unigrams],filename="test3")


def class_prob(corpora):
	probs = {}
	for author, corpus in corpora.items():
		probs[author] = sum([len(x) for x in corpus])
	M = sum(list(probs.values()))
	return {a : p/float(M) for a,p in probs.items()}


cprobs = class_prob(all_unigram)
sorted_cprobs = sort_dict(cprobs)
plot([Bar({"x" : list(zip(*sorted_cprobs))[0], "y": list(zip(*sorted_cprobs))[1]})],filename="test2")


def nbestimate(sentence):
	probs = []
	sprob = 0
	for author in uprobs:
		p = 1.0
		for word in sentence:
			p *= uprobs[author][word] 
		sprob += p
		probs += [(author, p * cprobs[author])]
	return probs, sprob


nbprobs, sprob = nbestimate(sentence)

plot([ Bar({"x" : list(zip(*sprobs))[0], "y": list(zip(*sprobs))[1]}),Bar({"x" : list(zip(*nbprobs))[0], "y": [i for i in list(zip(*nbprobs))[1]]})],filename="data")
nbmax = max(nbprobs, key= lambda x : x[1])
smax = max(sprobs, key= lambda x : x[1])
print(nbmax, smax)	