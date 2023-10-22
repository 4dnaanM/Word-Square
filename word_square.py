import random as rand
import re
class TrieNode:

    def __init__(self):
    
        self.children = [None]*26
        self.EOW = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def index(self,a:str):
        return ord(a)-ord('a')

    def insert(self,s:str):
        
        node = self.root
        
        for c in s:
            if(node.children[self.index(c)]==None):
                node.children[self.index(c)]=TrieNode()
        
            node = node.children[self.index(c)]
        
        node.EOW = True
        
        return True
    
    def findstart(self,s:str)->list:
        
        node = self.root
        
        for i in range(len(s)):
        
            if(node.children[self.index(s[i])]):
                node = node.children[self.index(s[i])]
        
            else:
                return False
        
        return True
    
    def find(self,s:str)->list:
        
        node = self.root
        
        for i in range(len(s)):
        
            if(node.children[self.index(s[i])]):
                node = node.children[self.index(s[i])]
        
            else:
                return False
        
        return node.EOW
    
class WordSquare():

    def __init__(self,s=None,symmetric=True,difficulty=5000):
        
        self.difficulty = difficulty
        self.symmetric = symmetric
        
        self.word_length = len(s) if s else 5
        words = self.stringmaker(self.word_length)
        
        self.wordlist = []
        
        with open(words,'r') as text:
        
            text_file = text.read().splitlines()
            
            for i in text_file:
                
                if(len(self.wordlist)>=self.difficulty):
                    break
            
                if(len(i)==self.word_length):
                    self.wordlist.append(i)
        
        self.trie = Trie()
        self.build_dictionary()

        self.square = [[None]*self.word_length for i in range(self.word_length)]
        self.squares = 0
        
        if(s==None):
            self.seed = self.wordlist[rand.randint(0,len(self.wordlist))]
        else: 
            self.seed = s.lower()
        
        for i in range(self.word_length):
            self.square[0][i]= self.seed[i]
            if(self.symmetric):self.square[i][0] = self.seed[i]
        
        print("Trying: %s with difficulty %d"%(self.seed.upper(),self.difficulty))
        
        self.guess(0)

        print("%d %s Word Square(s) of size %d Found for %s"%(self.squares,"Symmetric" if self.symmetric else "Unsymmetric",self.word_length,self.seed))

        return
    
    def stringmaker(self,num):
        return "/Users/Adnaan/Downloads/Diro_Behavior/Code/Word Square/dictionaries/words_final_"+str(num)+"_letter.txt"

    def build_dictionary(self):
        
        for i in self.wordlist:
            if(len(i)==self.word_length): self.trie.insert(i)
        
        return

    def printsquare(self):
        
        for row in range(self.word_length):
        
            for col in range(self.word_length):
                print(self.square[row][col].upper() if self.square[row][col] else " ",end=" ")
        
            print()
        
        print()
        
        return
    
    def guess(self,number):
        
        row = number//self.word_length
        col = number%self.word_length

        if number>=self.word_length*self.word_length:
        
            self.squares+=1
            self.printsquare()
            return
        
        if(self.square[row][col]!=None):
        
            self.guess(number+1)
            return
        
        row_word,col_word = '',''
        
        for r in range(row):
            col_word+=self.square[r][col]
        
        for c in range(col):
            row_word+=self.square[row][c]
        

        for alphabet in "abcdefghijklmnopqrstuvwxyz":
            
            if(self.trie.findstart(row_word+alphabet) and self.trie.findstart(col_word+alphabet)):
            
                self.square[row][col]=alphabet
            
                if(self.symmetric):self.square[col][row]=alphabet
            
                self.guess(number+1)
            
                self.square[row][col]=None
            
                if(self.symmetric):self.square[col][row]=None
    
if __name__=="__main__":
    
    word = "retina"
    
    difficulty = 8000
    
    try_word = WordSquare(word,True,difficulty)
    
    #try_word = WordSquare(word,False,difficulty)
