import re,operator
f = open('movies.txt')
unigram=re.findall('[A-Z]?[a-z]+|[A-Z]+|[0-9]+|[0-9]+th|[0-9]+st|[0-9]+rd|[0-9]+nd|[a-z]+-[a-z]+|Dr\.|Mr\.|Mrs\.|\'s|\'d|\.|,|&|\d{1,3}\.\d{1,3}\.\d{1,3}|[\w\.-]+@[\w\.\w]|http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|&',f.read())
print unigram

'''
-what is baum welch ? a spcl case of EM where E- steps are fwd and bkwrd & M steps are : calculating new prob based on o/p of fwd and backwrd algo
what are your obsv,
what is Expetation step &  what is  maximaization step
role of gamma and eta


'''