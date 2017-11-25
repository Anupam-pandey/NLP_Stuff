import re,operator
import sys
from collections import defaultdict
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *
from laplace import *
from kneser_ney import *
from witten_bell import *
import sys

filename=sys.argv[1]
gram=sys.argv[2]


if gram=="bigram":
	p1_KN,p2_KN=bigram_KN(filename)
	p1_WB,p2_WB=bigram_WB(filename)
	p1_ll,p2_ll,p3_ll,p4_ll,p5_ll=bigram_ll(filename)

	#plot([p1_KN, p2_KN,p1_WB,p1_WB,p1_ll,p2_ll,p3_ll,p4_ll,p5_ll],filename="bigrams")
	plot([p1_ll,p2_ll,p3_ll,p4_ll,p5_ll],filename="bigrams")

if gram=="unigram":
	#p1_WB,p2_WB=unigram_WB(filename)
	p1_ll,p2_ll,p3_ll,p4_ll,p5_ll=unigram_ll(filename)
	#plot([p1_WB,p1_WB,p1_ll,p2_ll,p3_ll,p4_ll,p5_ll],filename="unigrams")
	plot([p1_ll,p2_ll,p3_ll,p4_ll,p5_ll],filename="unigrams")


	


if gram=="trigram":
	p1_KN,p2_KN=trigram_KN(filename)
	p1_ll,p2_ll,p3_ll,p4_ll,p5_ll=trigram_ll(filename)
	p1_WB,p2_WB=trigram_WB(filename)
	#plot([p1_KN, p2_KN,p1_WB,p1_WB,p1_ll,p2_ll,p3_ll,p4_ll,p5_ll],filename="trigrams")
	plot([p1_ll,p2_ll,p3_ll,p4_ll,p5_ll],filename="trigrams")


	