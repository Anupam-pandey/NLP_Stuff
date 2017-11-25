import re,operator
import sys
from collections import defaultdict
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *


reverse_sorted_freq=[]
#filename=sys.argv[1]
def trigram(filename):
	f = open(filename)
	#unigram=re.sub('http[s]? : //(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(:%[0-9a-fA-F][0-9a-fA-F]))+',' ', f.read())
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ', f.read())
	unigram=re.sub('(\.)+','.', unigram)
	#unigram=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
	unigram=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|\.|,|\?|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
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
	V=sum(trigram_dict.values())
	reverse_sorted_trigrams=sorted(trigram_dict.items(),reverse=True,key=operator.itemgetter(1))
	return V,reverse_sorted_trigrams,trigram_dict


def unigram(filename):
	f = open(filename)
	unigram_dict=defaultdict(int)
	#unigram=re.sub('http[s]? : //(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(:%[0-9a-fA-F][0-9a-fA-F]))+',' ', f.read())
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ',f.read())
	unigram=re.sub('(\.)+','.', unigram)
	tokens=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|\?|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
	#tokens=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|,|&|2}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',f.read())
	unigram_dict={}
	for k in tokens:
		try:
			unigram_dict[k]+=1
		except:
			unigram_dict[k]=1
	V=len(tokens)
	reverse_sorted_unigrams=sorted(unigram_dict.items(),reverse=True,key=operator.itemgetter(1))
	return V,reverse_sorted_unigrams,unigram_dict



def bigram(filename):
	f = open(filename)
	unigram_dict=defaultdict(int)
	unigram_dict={}
	#unigram=re.sub('http[s]? : //(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(:%[0-9a-fA-F][0-9a-fA-F]))+',' ', f.read())
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ', f.read())
	unigram=re.sub('(\.)+','.', unigram)
	unigram=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|\.|\?|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)

	for k in unigram:
		try:
			unigram_dict[k]+=1
		except:
			unigram_dict[k]=1
	i=0
	j=1
	#V=len(tokens)
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
	V=sum(bigram_dict.values())
	reverse_sorted_bigrams=sorted(bigram_dict.items(),reverse=True,key=operator.itemgetter(1))
	return V,reverse_sorted_bigrams,bigram_dict




def wittenbell_bigram(bigramdict):
	prob_bidict={}
	type_dict=defaultdict(int)
	count_bidict=defaultdict(int)
	for k,v in bigramdict.items():
		first=k.strip().split()[0]
		temp=bigramdict[k]
		count_bidict[first]+=temp
		type_dict[first]+=1
	for k,v in bigramdict.items():
		first=k.strip().split()[0]
		prob_bidict[k]=round((bigramdict[k]/float(count_bidict[first]+type_dict[first])*count_bidict[first]),0)
	return prob_bidict

def wittenbell_trigram(trigramdict):
	prob_bidict={}
	type_dict=defaultdict(int)
	count_bidict=defaultdict(int)
	for k,v in trigramdict.items():
		first_list=k.strip().split()
		first=first_list[0]+" "+first_list[1]
		temp=trigramdict[k]
		count_bidict[first]+=temp
		type_dict[first]+=1
	for k,v in trigramdict.items():
		first_list=k.strip().split()
		first=first_list[0]+" "+first_list[1]
		prob_bidict[k]=round((trigramdict[k]/float(count_bidict[first]+type_dict[first])*count_bidict[first]),0)
	return prob_bidict


def Wittenbell(freq,V):
	prob_dict=defaultdict(int)
	T=len(freq)
	#print V,T
	for i in freq.keys():

		prob_dict[i]=round((freq[i]/float(V+T)*V),0)

	return prob_dict
	
#print unigram_dict
def bigram_WB(filename):
	V,reverse_sorted_bigrams,bigram_dict=bigram(filename)
	prob_bidict=wittenbell_bigram(bigram_dict)
	reverse_sorted__discounted_bigrams=sorted(prob_bidict.items(),reverse=True,key=operator.itemgetter(1))        
	p1 = Bar(x = list(zip(*reverse_sorted__discounted_bigrams))[0], y= list(zip(*reverse_sorted__discounted_bigrams))[1], name="Wittenbell_WBB")
	p2 = Bar(x = list(zip(*reverse_sorted_bigrams))[0], y= list(zip(*reverse_sorted_bigrams))[1], name="Unsmoothed_WBB")
	return p1,p2
	#plot([p1, p2],filename="WBB")#, p3, p4,p5])

def trigram_WB(filename):
	V,reverse_sorted_trigrams,trigram_dict=trigram(filename)
	prob_bidict=wittenbell_trigram(trigram_dict)
	reverse_sorted__discounted_trigrams=sorted(prob_bidict.items(),reverse=True,key=operator.itemgetter(1))        
	p1 = Bar(x = list(zip(*reverse_sorted__discounted_trigrams))[0], y= list(zip(*reverse_sorted__discounted_trigrams))[1], name="Wittenbell_WBT")
	p2 = Bar(x = list(zip(*reverse_sorted_trigrams))[0], y= list(zip(*reverse_sorted_trigrams))[1], name="Unsmoothed_WBT")
	return p1,p2
	#plot([p1, p2],filename="WBT")#, p3, p4,p5])


def unigram_WB(filename):
	V,reverse_sorted_unigrams,unigram_dict=unigram(filename)
	prob_dict=Wittenbell(unigram_dict,V)
	reverse_sorted__discounted_unigrams=sorted(prob_dict.items(),reverse=True,key=operator.itemgetter(1))        
	p1 = Bar(x = list(zip(*reverse_sorted__discounted_unigrams))[0], y= list(zip(*reverse_sorted__discounted_unigrams))[1], name="Wittenbell_WBU")
	p2 = Bar(x = list(zip(*reverse_sorted_unigrams))[0], y= list(zip(*reverse_sorted_unigrams))[1], name="Unsmoothed_WBU")
	return p1,p2
	#plot([p1, p2],filename="WBU")#, p3, p4,p5])


# bigram_WB()
# trigram_WB()
# unigram_WB()
