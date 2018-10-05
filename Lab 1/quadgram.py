from math import log10

class quadgramScore():
	def __init__(self):
		self.quadgrams = {}
		quadgram = open('english_quadgrams.txt')
		for gram in quadgram:
			text, value = gram.split(' ')
			self.quadgrams[text] = int (value)
		self.textLength = len(text)
		self.count = sum(self.quadgrams.values())

		keys = self.quadgrams.keys()
		for key in keys:
			self.quadgrams[key] = log10(float(self.quadgrams[key])/self.count)
		self.value = log10(0.01/self.count)

	def score(self, string):
		result = 0
		quadgrams = self.quadgrams.__getitem__
		for i in range(len(string) - self.textLength + 1):
			if string[i:i+self.textLength] in self.quadgrams:
				result += quadgrams(string[i:i+self.textLength])
			else:
				result += self.value

		return result

if __name__ == "__main__":
	fitness = quadgramScore()
	print(fitness.score('ejitpspawaqlejitaiulrtwllrflrllaoatwsqqjatgackthlsiraoatwlplqjatwjufrhlhutsqataqitatsaittkstqfjcae'))