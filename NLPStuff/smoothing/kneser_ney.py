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
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ',f.read())
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
	tokens=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|\?|\.|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
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
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ',f.read())
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



def KN_bigram(bigramdict,unigramdict):
	prob_bidict={}
	d=.05
	type_first_dict=defaultdict(int)
	type_second_dict=defaultdict(int)

	count_first_bidict=defaultdict(int)
	count_second_bidict=defaultdict(int)

	for k,v in bigramdict.items():
		first=k.strip().split()[0]
		second=k.strip().split()[1]

		temp=bigramdict[k]
		count_first_bidict[first]+=temp
		count_second_bidict[second]+=temp

		type_first_dict[first]+=1
		type_second_dict[second]+=1

	for k,v in bigramdict.items():
		first=k.strip().split()[0]
		second=k.strip().split()[1]
		try:
			prob_bidict[k]=((max(bigramdict[k]-d,0)/float(unigramdict[first]))+(d/float(unigramdict[first])*type_first_dict[first]*(type_second_dict[second]/float(len(bigramdict)))))
		except :
			prob_bidict[k]=(d/float(unigramdict[first]))*type_first_dict[first]*(type_second_dict[second]/float(len(bigramdict)))
		prob_bidict[k]*=unigramdict[first]
	return prob_bidict

def KN_trigram(trigramdict,bigramdict):
	prob_bidict={}
	d=.5
	type_first_dict=defaultdict(int)
	type_second_dict=defaultdict(int)
	type_third_dict=defaultdict(int)


	count_firstsecond_dict=defaultdict(int)
	count_second_dict=defaultdict(int)
	count_third_dict=defaultdict(int)


	for k,v in trigramdict.items():
		first=k.strip().split()[0]
		second=k.strip().split()[1]
		third=k.strip().split()[2]
		first=first+" "+second


		#print k,v
		temp=trigramdict[k]
		count_firstsecond_dict[first]+=temp
		count_second_dict[second]+=temp
		count_third_dict[third]+=temp


		type_first_dict[first]+=1
		type_second_dict[second]+=1
		type_second_dict[third]+=1


	for k,v in trigramdict.items():
		first=k.strip().split()[0]
		second=k.strip().split()[1]
		third=k.strip().split()[2]
		first=first+" "+second
		

		try:
			prob_bidict[k]=((max(trigramdict[k]-d,0)/float(bigramdict[first]))+(d/float(bigramdict[first])*type_first_dict[first]*(type_third_dict[third]/float(len(trigramdict)))))
		except :
			prob_bidict[k]=(d/float(bigramdict[first]))*type_first_dict[first]*(type_third_dict[third]/float(len(trigramdict)))
		prob_bidict[k]*=bigramdict[first]
	return prob_bidict


#print unigram_dict
def bigram_KN(filename):
	V,reverse_sorted_bigrams,bigram_dict=bigram(filename)
	Vuni,reverse_sorted_unigrams,unigram_dict=unigram(filename)
	prob_bidict=KN_bigram(bigram_dict,unigram_dict)
	reverse_sorted__discounted_bigrams=sorted(prob_bidict.items(),reverse=True,key=operator.itemgetter(1))        
	p1 = Bar(x = list(zip(*reverse_sorted__discounted_bigrams))[0], y= list(zip(*reverse_sorted__discounted_bigrams))[1], name="KN_KNB")
	p2 = Bar(x = list(zip(*reverse_sorted_bigrams))[0], y= list(zip(*reverse_sorted_bigrams))[1], name="Unsmoothed_KNB")
	return p1,p2
	#plot([p1, p2])#, p3, p4,p5])

def trigram_KN(filename):
	V,reverse_sorted_trigrams,trigram_dict=trigram(filename)
	V,reverse_sorted_bigrams,bigram_dict=bigram(filename)
	

	prob_bidict=KN_trigram(trigram_dict,bigram_dict)
	reverse_sorted__discounted_trigrams=sorted(prob_bidict.items(),reverse=True,key=operator.itemgetter(1))        
	p1 = Bar(x = list(zip(*reverse_sorted__discounted_trigrams))[0], y= list(zip(*reverse_sorted__discounted_trigrams))[1], name="KN_KNT")
	p2 = Bar(x = list(zip(*reverse_sorted_trigrams))[0], y= list(zip(*reverse_sorted_trigrams))[1], name="Unsmoothed_KNT")
	return p1,p2
	#plot([p1, p2],filename="test")#, p3, p4,p5])


# bigram_KN()
# trigram_KN()

