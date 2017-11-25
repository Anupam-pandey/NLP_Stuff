import re,operator
import sys
import math
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *
from collections import defaultdict

f = open(sys.argv[1])
gram=sys.argv[2]
if gram=="trigram":
	#unigram=re.sub('http[s]? : //(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',' ', f.read())
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ', f.read())
	unigram=re.sub('(\.)+','.', unigram)

	#unigram=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)


	unigram=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Phd\.|Mr\.|Mrs\.|\'s|\'d|\.|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
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
	sumval=sum(trigram_dict.values())
	reverse_sorted_trigrams=sorted(trigram_dict.items(),reverse=True,key=operator.itemgetter(1))        

	# bg=sorted(trigram_dict,key=trigram_dict.get,reverse=True)
	bg2=[]
	# for i in range(len(bg)):
	# 	bg2.append(trigram_dict[bg[i]])
	# rankdict={}
	# j=1;
	#print reverse_sorted_trigrams
	rank=[]
	logg=[]
	for i in xrange(len(reverse_sorted_trigrams)):
		rank.append(i+1)
		#print reverse_sorted_trigrams[i][1]
		#temp=float(reverse_sorted_trigrams[i][1])/float(sumval)
		temp=float(reverse_sorted_trigrams[i][1])
		logg.append(float(math.log(temp,10)))
	# for i in reverse_sorted_trigrams[0]:
	# 	rankdict[j]=i;
	# 	j+=1;
	# print bg2
	# for k,v in bigram_dict.items():
	# 	print k,v
	# for i in reverse_sorted_trigrams:
	# 	print i
	# tg = sorted(trigram_dict, key=trigram_dict.get, reverse=True)
	# tg2=[]
	# for i in range(len(tg)):
	# 	tg2.append(trigram_dict[tg[i]])


	# for k,v in trigram_dict.items():
	# 	print k,v
	#init_notebook_mode(connected=True)

	plot([{"x" : list(zip(*reverse_sorted_trigrams))[0], "y": list(zip(*reverse_sorted_trigrams))[1]}],filename="ziphs.html")
	plot([{"x" : rank, "y": logg}],filename="logcurve.html")



elif gram=="unigram":
	unigram_dict=defaultdict(int)
	#unigram=re.sub('http[s]? : //(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',' ', f.read())
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ',f.read())
	unigram=re.sub('(\.)+','.', unigram)
	tokens=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|\.|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
	#tokens=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|,|&|2}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',f.read())
	unigram_dict={}
	for k in tokens:
		try:
			unigram_dict[k]+=1
		except:
			unigram_dict[k]=1


	reverse_sorted_unigrams=sorted(unigram_dict.items(),reverse=True,key=operator.itemgetter(1))        
	# for k in reverse_sorted_unigrams:
	# 	print k
	rank=[]
	logg=[]
	for i in xrange(len(reverse_sorted_unigrams)):
		rank.append(i+1)
		#print reverse_sorted_trigrams[i][1]
		#temp=float(reverse_sorted_trigrams[i][1])/float(sumval)
		temp=float(reverse_sorted_unigrams[i][1])
		logg.append(float(math.log(temp,10)))
	#init_notebook_mode(connected=True)
	plot([{"x" : list(zip(*reverse_sorted_unigrams))[0], "y": list(zip(*reverse_sorted_unigrams))[1]}])
	plot([{"x" : rank, "y": logg}],filename="logcurve.html")
	
elif gram=="bigram":
	unigram_dict=defaultdict(int)
	unigram_dict={}
	#unigram=re.sub('http[s]? : //(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',' ', f.read())
	unigram=re.sub('(&gt)+|(&amp)+|(&lt)+|(&nbsp)+',' ', f.read())
	unigram=re.sub('(\.)+','.', unigram)
	unigram=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|\.|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',unigram)
	# print unigram
	# print type(unigram)
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

	# bg=sorted(bigram_dict,key=bigram_dict.get,reverse=True)
	# bg2=[]
	# for i in range(len(bg)):
	# 	bg2.append(bigram_dict[bg[i]])
	# for k,v in bigram_dict.items():
	# 	print k,v

	# for i in reverse_sorted_bigrams:
	# 	print i
	#init_notebook_mode(connected=True)
	rank=[]
	logg=[]
	for i in xrange(len(reverse_sorted_bigrams)):
		rank.append(i+1)
		#print reverse_sorted_trigrams[i][1]
		#temp=float(reverse_sorted_trigrams[i][1])/float(sumval)
		temp=float(reverse_sorted_bigrams[i][1])
		logg.append(float(math.log(temp,10)))
	plot([{"x" : list(zip(*reverse_sorted_bigrams))[0], "y": list(zip(*reverse_sorted_bigrams))[1]}])
	plot([{"x" : rank, "y": logg}],filename="logcurve.html")
	
