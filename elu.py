import nltk
from nltk.tree import Tree
from nltk.draw.tree import TreeView
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> AdvP NP | N VP | N
AdvP -> Adv
Adv -> "when"
VP -> V NP 
N -> "Mum" | "Ade" | "dinner"
V -> "smiled" | "made"
""")
sent = "Mum smiled when Ade made dinner".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sent):
    print(tree)
treestring = str(tree)
t = Tree.fromstring(treestring)
TreeView(t)._cframe.print_to_file('output.ps')
