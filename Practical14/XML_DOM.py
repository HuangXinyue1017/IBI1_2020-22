import xml.dom.minidom
from xml.dom.minidom import parse
import matplotlib.pyplot as plt
import re
import os

class node:
	def __init__(self,id,fe):
		self.id = id
		self.fa_list = [] # all fathers of this node
		self.ch_list = [] # all children of this node
		self.feature = fe # DNA / RNA / protein / other molecule
		self.flag = False # whether this node has been added or not

def link(fa,ch):
	# two-way link
	fa.ch_list.append(ch)
	ch.fa_list.append(fa)

def parse_xml(path):
	# parse the XML file into a DOM document object
	DOMTree = xml.dom.minidom.parse(path)
	# get the root element of the document
	collection = DOMTree.documentElement
	# get a list of 'term' elements
	terms = collection.getElementsByTagName("term")
	return terms

def count(now,fe):
	now.flag = True
	for ch in now.ch_list:
		# subtract the middle nodes
		if(ch.feature.find(fe) != -1):
			sub[ch.id] = 1
		# find all the related nodes
		if(ch.flag == False):
			count(ch,fe)

def calculate(fe):
	# initialize and counted the nodes with feature
	sub.clear()
	related_node = 0
	for now in node_dict.values():
		now.flag = False
		if(now.feature.find(fe) != -1):
			related_node += 1

	# mark all the related nodes and their childnodes
	for now in node_dict.values():
		if(now.feature.find(fe) != -1 and now.flag == False):
			count(now,fe)

	# count all the related nodes and their childnodes
	all_node = 0
	for now in node_dict.values():
		if(now.flag == True):
			all_node += 1

	return all_node - related_node + len(sub)

def build_graph(terms):
	# build all nodes
	for term in terms:
		node_id = term.getElementsByTagName("id")[0].childNodes[0].data
		def_text = term.getElementsByTagName("defstr")[0].childNodes[0].data
		node_dict[node_id] = node(node_id,def_text)

	# links nodes
	for term in terms:
		node_id = term.getElementsByTagName("id")[0].childNodes[0].data
		fathers = [father.childNodes[0].data for father in term.getElementsByTagName("is_a")]
		for fa_id in fathers:
			link(node_dict[fa_id],node_dict[node_id])
	return

# define absolute file path
path = "C:\\Users\\86186\\Desktop\\test\\go_obo.xml"

# parse the XML file
terms = parse_xml(path)

# build tree
node_dict = {}
build_graph(terms)

# calculate the answer
sub = {}
DNA = calculate("DNA")
RNA = calculate("RNA")
PRO = calculate("protein")
OTHER = calculate("carbohydrate")

print("Number of child nodes of DNA-associated terms: %d" % DNA)
print("Number of child nodes of RNA-associated terms: %d" % RNA)
print("Number of child nodes of protein-associated terms: %d" % PRO)
print("Number of child nodes of carbohydrate-associated terms: %d" % OTHER)

# plot the pie chart
labels = ['DNA-associated','RNA-associated terms', \
		  'Protein-associated terms','carbohydrate-associated']
values = [DNA,RNA,PRO,OTHER]
explode = (0,0.1,0,0)
plt.pie(values, explode = explode, labels = labels,	autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.title("The number of child nodes of four kinds of molecules")
plt.show()