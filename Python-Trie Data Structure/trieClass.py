#LastName: Lamichhane
#FirstName: Rasmi
#Email: rala8730@colorado.edu
#Comments: this is hard 

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):#
        assert(len(w)>=0)
        # YOUR CODE HERE
        # If you want to create helper/auxiliary functions, please do so.
        if(len(w)==0):
            self.isWordEnd=True
            self.count+=1
        else:
            c=w[0]#c=1st element
            w=w[1:]#w=from 2nd element to end
            if c not in self.next:#if c is not in root
                self.next[c]=MyTrieNode(False)#make a new node
            self.next[c].addWord(w)#
        #add word to retriveie it later
        return

    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.

        # YOUR CODE HERE
        mycount=0
        assert(len(w)>=0)
        if(len(w)==0):
            if self.isWordEnd==True:
                mycount=self.count
        else:
            c=w[0]
            w=w[1:]
            if c not in self.next:
                mycount=0
            else:
                mycount=self.next[c].lookupWord(w)
        return mycount
        #0 # TODO: change this line, please

    def autoComplete(self,w):

        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #word s occurs with frequency j
        #YOUR CODE HERE
        root=self
        l=[]
        for prefix in w:
            if prefix not in self.next:
                return l
            else:
                self=self.next[prefix]
        a=self.DFS(P=l)
        a=set(a)
        assert(len(w)>=0)
        listofword=[]
        print(a)
        for word in a:
            listofword.append((w+word,root.lookupWord(w+word)))
        #return al of the word with prefix of w
        return(listofword)#[('Walter',1),('Mitty',2),('Went',3),('To',4),('Greenland',2)] #TODO: change this line, please'
                
    def DFS(self,prefix="",P=[]):
        #p=[]
        if self.isWordEnd:
            #print(prefix)
            #for i in prefix:
            P.append(prefix)

            #print(set(p),"set p")
        for c in self.next:
            self.next[c].DFS(prefix + c,P=P)
        P=set(P)
        #print(P)
        return(P)

if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    t.DFS()
    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
