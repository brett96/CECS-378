'''
Allows scoring of text using n-gram probabilities
17/07/12
'''
from math import log10
from random import shuffle


class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        ngram = open(ngramfile)
        for line in ngram:
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        print(self.L)
        print(key)
        self.N = sum(self.ngrams.values())
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score

    def decrypt(self, string):
        alphaMap = {"a": "", "b":"", "c":"", "d":"", "e":"", "f":"", "g":"", "h":"", "i":"", "j":"", "k":"", "l":"", "m":"", "n":"", "o":"", "p":"", "q":"", 
        "r":"", "s":"", "t":"", "u":"", "v":"", "w":"", "x":"", "y":"", "z":""} 

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key = list(alphabet)
        shuffle(key)

        for i in range(0, len(alphaMap)):
            alphaMap[alphabet[i]] = key[i]

        result = ""
        for i in range(0, len(string)):
            result += alphaMap[string[i]] 

        score = self.score(result)
        return result
        #return score
        
       
if __name__ == '__main__':
    fitness = ngram_score('english_quadgrams.txt')
    print(fitness.decrypt("ejitpspawaqlejitaiulrtwllrflrllaoatwsqqjatgackthlsiraoatwlplqjatwjufrhlhutsqataqitatsaittkstqfjcae"))
    # print(fitness.score("ATTACK THE EAST WALL OF THE CASTLE AT DAWN"))
    # print(fitness.score("ATTACKTHEEASTWALLOFTHECASTLEATDAWN"))
    # print(fitness.score("SHGIFGHISFGBNLEOJRVEHGOBRIWHNBIRHW"))