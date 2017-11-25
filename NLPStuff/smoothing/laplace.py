import re,operator
import sys
from collections import defaultdict
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *

#filename=sys.argv[1]
reverse_sorted_freq=[]

def LaplaceSmoothing(freq,V):
	N=sum(freq.values())
	for val in freq:
		freq[val]=round((freq[val]+1)/float(N+V),15)*N
	return freq

def bigram_ll(filename):
	f = open(filename)
	unigram_dict=defaultdict(int)
	unigram_dict={}
	#unigram=re.sub('http[s]? : //(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',' ', f.read())
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ', f.read())
	unigram=re.sub('(\.)+','.', unigram)
	unigram=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|\.|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)

	for k in unigram:
		try:
			unigram_dict[k]+=1
		except:
			unigram_dict[k]=1
	i=0
	j=1
	length=len(unigram)-1
	bigram=[]
	while j<=length:
		s=unigram[i]+' '+unigram[j]
		bigram.append(s)
		i=i+1
		j=j+1

	bigram_dict={}	
	for k in bigram:
		if k in bigram_dict:
			bigram_dict[k]+=1
		else:
			bigram_dict[k]=1

	bg=[]
	reverse_sorted_bigrams=sorted(bigram_dict.items(),reverse=True,key=operator.itemgetter(1))        

	freq= LaplaceSmoothing(bigram_dict,200)
	smoothed_200=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))        
	freq= LaplaceSmoothing(bigram_dict,2000)
	smoothed_2000=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))        
	freq= LaplaceSmoothing(bigram_dict,len(bigram_dict))
	smoothed_double=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))        
	freq= LaplaceSmoothing(bigram_dict,len(bigram_dict)*10)
	smoothed_10_double=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))
	p1 = Bar(x = list(zip(*reverse_sorted_bigrams))[0], y= list(zip(*reverse_sorted_bigrams))[1], name="unsmoothed_LLB")
	p2 = Bar(x = list(zip(*smoothed_200))[0], y= list(zip(*smoothed_200))[1], name="200")
	p3 = Bar(x = list(zip(*smoothed_2000))[0], y= list(zip(*smoothed_2000))[1],  name="2000")
	p4 = Bar(x = list(zip(*smoothed_double))[0], y= list(zip(*smoothed_double))[1], name="N")
	p5 = Bar(x = list(zip(*smoothed_10_double))[0], y= list(zip(*smoothed_10_double))[1],  name="10* N")
	return p1,p2,p3,p4,p5
	#plot([p1, p2, p3, p4,p5],filename="LLB")

def trigram_ll(filename):
	f = open(filename)
	#unigram=re.sub('http[s]? : //(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',' ', f.read())
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ', f.read())
	unigram=re.sub('(\.)+','.', unigram)
	#unigram=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
	unigram=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|\.|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
	unigram_dict={}
	for k in unigram:
		if k in unigram_dict:
			unigram_dict[k]+=1
		else:
			unigram_dict[k]=1
	trigram=[]
	i=0
	j=1
	length=len(unigram)-1
	k=2
	while k<=length:
		s=unigram[i]+' '+unigram[j]+' '+unigram[k]
		trigram.append(s)
		i=i+1
		j=j+1
		k=k+1

	trigram_dict={}
	for k in trigram:
		if k in trigram_dict:
			trigram_dict[k]+=1
		else:
			trigram_dict[k]=1

	tg=[]

	reverse_sorted_trigrams=sorted(trigram_dict.items(),reverse=True,key=operator.itemgetter(1))
	freq= LaplaceSmoothing(trigram_dict,200)
	smoothed_200=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))        
	freq= LaplaceSmoothing(trigram_dict,2000)
	smoothed_2000=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))        
	freq= LaplaceSmoothing(trigram_dict,len(trigram_dict))
	smoothed_double=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))        
	freq= LaplaceSmoothing(trigram_dict,len(trigram_dict)*10)
	smoothed_10_double=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))
	p1 = Bar(x = list(zip(*reverse_sorted_trigrams))[0], y= list(zip(*reverse_sorted_trigrams))[1],  name="unsmoothed_LLT")
	p2 = Bar(x = list(zip(*smoothed_200))[0], y= list(zip(*smoothed_200))[1], name="200")
	p3 = Bar(x = list(zip(*smoothed_2000))[0], y= list(zip(*smoothed_2000))[1], name="2000")
	p4 = Bar(x = list(zip(*smoothed_double))[0], y= list(zip(*smoothed_double))[1], name="N")
	p5 = Bar(x = list(zip(*smoothed_10_double))[0], y= list(zip(*smoothed_10_double))[1],name="10* N")
	return p1,p2,p3,p4,p5

	#plot([p1, p2, p3, p4,p5],filename="LLT")

def unigram_ll(filename):
	f = open(filename)
	unigram_dict=defaultdict(int)
	#unigram=re.sub('http[s]? : //(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',' ', f.read())
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ', f.read())
	unigram=re.sub('(\.)+','.', unigram)
	tokens=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
	#tokens=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|,|&|2}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',f.read())
	unigram_dict={}
	for k in tokens:
		try:
			unigram_dict[k]+=1
		except:
			unigram_dict[k]=1
	reverse_sorted_unigrams=sorted(unigram_dict.items(),reverse=True,key=operator.itemgetter(1))        
	freq= LaplaceSmoothing(unigram_dict,200)
	smoothed_200=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))        
	freq= LaplaceSmoothing(unigram_dict,2000)
	smoothed_2000=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))        
	freq= LaplaceSmoothing(unigram_dict,len(unigram_dict))
	smoothed_double=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))        
	freq= LaplaceSmoothing(unigram_dict,len(unigram_dict)*10)
	smoothed_10_double=sorted(freq.items(),reverse=True,key=operator.itemgetter(1))
	p1 = Bar(x = list(zip(*reverse_sorted_unigrams))[0], y= list(zip(*reverse_sorted_unigrams))[1], name="unsmoothed_LLU")
	p2 = Bar(x = list(zip(*smoothed_200))[0], y= list(zip(*smoothed_200))[1], name="200")
	p3 = Bar(x = list(zip(*smoothed_2000))[0], y= list(zip(*smoothed_2000))[1],  name="2000")
	p4 = Bar(x = list(zip(*smoothed_double))[0], y= list(zip(*smoothed_double))[1],name="N")
	p5 = Bar(x = list(zip(*smoothed_10_double))[0], y= list(zip(*smoothed_10_double))[1],  name="10* N")
	return p1,p2,p3,p4,p5

	#plot([p1, p2, p3, p4,p5],filename="LLU")



#bigram_ll()
# unigram_ll()
# trigram_ll()