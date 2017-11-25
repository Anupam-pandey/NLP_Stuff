#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import *
import os
import sys  
reload(sys)
sys.setdefaultencoding('utf8')
from  nltk.corpus import brown
from collections import defaultdict
import math

# A = {'cp' :{'cp' : 0.7, 'ip' : 0.3},'ip' :{'cp' : 0.5, 'ip' : 0.5}}
# B = {'cp' :{'Cola' : 0.6, 'ice_tea' : 0.1, 'lemonade' : 0.3},'ip' :{'Cola' : 0.1, 'ice_tea' : 0.7, 'lemonade' : 0.2}}
# pi={'cp':1,'ip': 0}

# alphas=defaultdict(list)
# betas=defaultdict(list)


# observation=["woods","clotted",]
# for state in pi:
# 	alphas[state].append(pi[state])

def forward_procedure(observation,A,B,pi,alphas):
	index=0
	for sequence in observation:
		for state in A:
			probability_sum=0
			for transistion in A:
				probability_sum+= A[transistion][state]* B[transistion][sequence]*alphas[transistion][index]
			alphas[state].append((probability_sum))
		index+=1
	return alphas	

# for x in xrange(len(observation)+2):
# 	for state in pi:
# 		betas[state].append(1)

# for state in pi:
# 		betas[state][0]=pi[state]

def backward_procedure(observation,A,B,pi,betas):
	index=len(observation)+1
	for sequence in observation:
		for state in A:
			probability_sum=0
			for transistion in A:
#				print state ,sequence,transistion,A[state][transistion], B[state][sequence],betas[transistion][index]
				probability_sum+= A[state][transistion]* B[state][sequence]*betas[transistion][index]
			betas[state][index-1]=probability_sum
		index-=1
	return betas

# alphas=forward_procedure(observation,A,B,pi,alphas)
# Alpha_prob=0
# for state in pi:
# 		Alpha_prob+=alphas[state][len(observation)]

# observation.reverse()

# betas=backward_procedure(observation,A,B,pi,betas)
# for state in pi:
# 		betas[state]=betas[state][1:]
# Beta_prob=0		
# for state in pi:
# 		Beta_prob+=betas[state][0]*pi[state]

# observation.reverse()

def baum_welch(observation,A,B,Allalphas,Allbetas,Alpha_prob):
	prob_state_list=[]
	gamma_state_list=[]
	P_i_j=defaultdict(list)
	gamma=defaultdict(int)

	for timesequence in xrange(len(observation)):
		temp={}
		temp2={}
		for state in A:
			for transistion in A:
				#print timesequence, state,transistion,observation[timesequence], Allalphas[state][timesequence] , A[state][transistion] , B[state][observation[timesequence]] , Allbetas[transistion][timesequence + 1],
				prob_state=(Allalphas[state][timesequence] * A[state][transistion] * B[state][observation[timesequence]] * Allbetas[transistion][timesequence + 1])/Alpha_prob
				#print prob_state			
				temp[transistion]=prob_state
			#print temp
			temp2[state]=temp
			temp={}
		#print temp2
		for k,v in temp2.items():
			res=0
			for k2,v2 in v.items():
			#	print k,k2,v2
				res+=v2
			#print res
			gamma[k]=res
		#print gamma
		gamma_state_list.append(gamma)
		gamma={}
		P_i_j=temp2.copy()
		prob_state_list.append(P_i_j)
		temp2={}		
		P_i_j=defaultdict(list)

	return gamma_state_list,prob_state_list		

def normalize(A):
	for k,v in A.items():
		res=0;
		for k2,v2 in v.items():
			res+=v2
		for k3,v3 in v.items():
			A[k][k3] =A[k][k3]/res
	return A

# gamma_state_prob_list,zeta_prob_state_list=baum_welch(observation,A,B,alphas,betas,Alpha_prob)

def A_New(A,observation,zeta_prob_state_list,gamma_state_prob_list):
	for state in A:
		for transistion in A:
			gammasum=0
			res=0
			for sequence in xrange(len(observation)):
				res+=zeta_prob_state_list[sequence][state][transistion]
				gammasum+=gamma_state_prob_list[sequence][state]		
			A[state][transistion]=res/gammasum
	return A	

def pi_new(A,pi,gamma_state_prob_list):
	res=0
	for state in A:
		pi[state]=gamma_state_prob_list[0][state]
		res+=gamma_state_prob_list[0][state]
	for state in A:
		pi[state]=pi[state]/res	
	return pi


def getB_keys(B):
	emissionkeys=[]
	for k,v in B.items():
		for k2,v2 in v.items():
			emissionkeys.append(k2)
	return emissionkeys


def B_new(A,B,observation,gamma_state_prob_list):
	emissionkeys=getB_keys(B)
	for transistion in A:
		for emission in emissionkeys:
			gammasum=0
			res=0
			for sequence in xrange(len(observation)):
				if observation[sequence]==emission:
					res+=gamma_state_prob_list[sequence][transistion]
				gammasum+=gamma_state_prob_list[sequence][transistion]		
			B[transistion][emission]=res/gammasum
	return B

# A=A_New(A,observation,zeta_prob_state_list,gamma_state_prob_list)	
# pi=pi_new(A,pi,gamma_state_prob_list)
# B=B_new(A,B,observation,gamma_state_prob_list)
# A=normalize(A)
# B=normalize(B)

# print pi
# print A
# print B

def generatePI(states):
	pi=defaultdict(int)
	for sequence in xrange(states):

		pi["tag"+str(sequence)]=random()
	res=0
	for k,v in pi.items():
		res+=v;
	for k,v in pi.items():
		pi[k]=pi[k]/res
		
	return pi

def generate_A(words,states):
	A=defaultdict(dict)
	for sequence in xrange(states):
		temp={}
		for sequence2 in xrange(states):
			temp["tag"+str(sequence2)]=random()
		A["tag"+str(sequence)]=temp
	normalize(A)
	return A	


def generate_B(words,states):
	B=defaultdict(dict)
	for sequence in xrange(states):
		temp={}
		for sequence2 in words:
			temp[sequence2]=random()
		B["tag"+str(sequence)]=temp
	normalize(B)
	return B	

def manageData(words,states):
	for  i in xrange(1):
		observation=brown.sents()[0]
		observation=[key.strip().lower().encode('utf-8') for key in observation]

		alphas=defaultdict(list)
		betas=defaultdict(list)
		#print words
		print len(words)
		tokens=[key.strip().lower().encode('utf-8') for key in words]
		#print len(tokens),type(tokens)
		vocabulary=list(set(tokens))
		print len(vocabulary)
		pi=generatePI(states)
		#print pi
		A=generate_A(vocabulary,states)
		#print A
		B=generate_B(vocabulary,states)
		#print len(B['tag0']) , "------------"
		
		# print "before calculation A & B"	
		A=normalize(A)
		B=normalize(B)
		#print A

		# print B
		for state in pi:
			alphas[state].append(pi[state])
		alphas=forward_procedure(observation,A,B,pi,alphas)
		Alpha_prob=0
		for state in pi:
				Alpha_prob+=alphas[state][len(observation)]
				#print alphas[state][len(observation)]

		print Alpha_prob, " initial prob"	
	#	print alphas

		observation.reverse()

		for x in xrange(len(observation)+2):
			for state in pi:
				betas[state].append(1)

		for state in pi:
				betas[state][0]=pi[state]


		betas=backward_procedure(observation,A,B,pi,betas)
		for state in pi:
				betas[state]=betas[state][1:]

		Beta_prob=0		
		for state in pi:
				Beta_prob+=betas[state][0]*pi[state]

		observation.reverse()
		#print alphas
		for j in xrange(20):
			#print len(A),len(B),len(alphas),len(betas)
			gamma_state_prob_list,zeta_prob_state_list=baum_welch(observation,A,B,alphas,betas,Alpha_prob)

			A=A_New(A,observation,zeta_prob_state_list,gamma_state_prob_list)	
			pi=pi_new(A,pi,gamma_state_prob_list)
			B=B_new(A,B,observation,gamma_state_prob_list)
			A=normalize(A)
			B=normalize(B)
			
			# print "pi----------------------------"
			# print pi
			# print 
			# print "A----------------------------"

			# print A
			# print 
			# print "B----------------------------"

			# print B
			alphas=defaultdict(list)
			betas=defaultdict(list)


			for state in pi:
				alphas[state].append(pi[state])

			alphas=forward_procedure(observation,A,B,pi,alphas)
			#print "--------------------------------"
			#print alphas
			Alpha_prob=0
			for state in pi:
					Alpha_prob+=alphas[state][len(observation)]
					#print alphas[state][len(observation)]
			print Alpha_prob, " final prob"
			observation.reverse()
			for x in xrange(len(observation)+2):
				for state in pi:
					betas[state].append(1)

			for state in pi:
					betas[state][0]=pi[state]
			betas=backward_procedure(observation,A,B,pi,betas)
			for state in pi:
					betas[state]=betas[state][1:]

			Beta_prob=0		
			for state in pi:
					Beta_prob+=betas[state][0]*pi[state]

			observation.reverse()









test=[]
#manageData(brown.words(),10)
# with open("dataset") as f:
# 	line= f.read().split()
# 	for x in line:
# 		test.append(x)



manageData(brown.words(),10)

# print Alpha_prob , Beta_prob 
# print alphas
# print betas
#print betas


