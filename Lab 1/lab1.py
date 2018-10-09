import operator
from random import shuffle

def encrypt(string, key):  # Key being used by me is "fpaijnewxtslkdyqzmhrgovbcu"
	string = string.lower()
	cArray = list(string)
	keyArray = list(key)

	alphaMap = {"a": "", "b":"", "c":"", "d":"", "e":"", "f":"", "g":"", "h":"", "i":"", "j":"", "k":"", "l":"", "m":"", "n":"", "o":"", "p":"", "q":"", 
		"r":"", "s":"", "t":"", "u":"", "v":"", "w":"", "x":"", "y":"", "z":""}  #Mapping of all letters

	alphabet = "abcdefghijklmnopqrstuvwxyz"

	for char in cArray:
		if char == " " or char.isalpha() == False:
			cArray.remove(char)  # Strips whitespace and non alphabetic characters in string

	i = 0
	for char in keyArray:
		if char == " ":
			keyArray.remove(char)	# Strips whitespace in key
		else:
			alphaMap[alphabet[i]] = char # Maps the standard alphabet to the provided key in order
			i += 1

	for i in cArray:  # Remove whitespace
		if i == ' ':
			cArray.remove(i)

	result = ""
	for char in cArray:
		result += alphaMap[char]
	print(result)


def convertToNum(string):
	string = string.lower()
	result = ""
	num = 1
	string = list(string)
	chars = {"a": "", "b":"", "c":"", "d":"", "e":"", "f":"", "g":"", "h":"", "i":"", "j":"", "k":"", "l":"", "m":"", "n":"", "o":"", "p":"", "q":"", 
		"r":"", "s":"", "t":"", "u":"", "v":"", "w":"", "x":"", "y":"", "z":""}
	for char in string:
		if chars[char] == "":
			chars[char] = num
			result += str(num) + " "
			num += 1
		else:
			result += str(chars[char]) + " "
	#result = result[0:len(result) - 1]
	return result




def isWord(word, words, start, stop):  #Searches for word in dictionary using binary search
	if stop >= start:
		idx = int(start + (stop-start) / 2)
		if words[idx].lower() == word.lower():
			return True

		elif words[idx].lower() > word.lower():
			return isWord(word, words, 1, idx-1)

		else:
			return isWord(word, words, idx+1, stop)
	else:
		return False

def getAllMatches(nDict, string):
	indexes = [i for i, x in enumerate(nDict) if x == string]
	return indexes



def decrypt(string):
	cArray = list(string)
	common = "etaoinshrdlucmwfgypbvkjxqz"  #frequent letters in english

	# Tries all possibilities of a shift cipher

	for char in cArray:
		if char == " ":
			cArray.remove(char)  #Strips whitespace
	string = "".join(cArray)
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	dictFile = open("dictionary.txt", "r")  # opens file w/ list of english words (dictionary)
	words = dictFile.read()
	words = words.split("\n")  # Split all words in the file into a list
	for i in range(0, 26):
		for j in range(0, len(cArray)):
			cArray[j] = alphabet[(alphabet.find(cArray[j]) + 1) % 26] # Increments letter by 1
		message = "".join(cArray[0:2])  # Initializes message to the first 2 chars in the text
		for k in range(2, len(cArray)): 
			#print(message)
			if isWord(message, words, 0 , len(words)-1):  # Check if current message matches any words in the dictionary list
				print("".join(cArray) + "  :  Shift = " + str(i+1) + "\n\n") # Possible message
				break
			message += cArray[k]  # Add another char to the message and try again

	cipherNum = convertToNum(string)

	cipherNum = cipherNum.split(" ")
	#print(cipherNum)

	# wordNumFile = open("wordNums.txt", "w")
	# numFile = open("nums.txt", "w")
	nums = []
	for word in words:
		# wordNumFile.write(word + " " + convertToNum(word) + "\n")
		# numFile.write(convertToNum(word) + "\n")
		nums.append(convertToNum(word))


	
	length = len(cipherNum) 
	
	possibleWord = ""
	for i in range(0, len(cipherNum)):
		#possibleWord = ""
		possibleWord += cipherNum[i] + " "
		matches = getAllMatches(nums, possibleWord) #[i for i, x in enumerate(nums) if x == possibleWord] # List of all words that match the current pattern

		# for each match, try finding a next word starting from the next character
		for match in matches:
			# print(words[match])
			nextWordIdx = i + 1
			nextWord = ""
			for j in range(nextWordIdx, len(cipherNum)):  # need to start new pattern from 1; currently starting next word w/ pattern history from previous word
				nextWord += cipherNum[j] + " "
				print(nextWord)
				nextMatches = getAllMatches(nums, nextWord)  # List of all pattern matches for next word
				for nextMatch in nextMatches:
					print(words[match] + " " + words[nextMatch])

# Redo
	# while length > 0:
	# 	word = ""
	# 	for c in range(0, length):
	# 		word += cipherNum[c] + " "
			
	# 	indexes = [i for i, x in enumerate(nums) if x == word] # List of all words that match the current pattern
	# 	for index in indexes:  # Go through each item in list & use as possible word
	# 		result = words[index]
	# 		nextWord = ""
	# 		for d in range(len(str(words[index])), len(cipherNum)):
	# 			nextWord += cipherNum[d] + " "

	# 		nextIndexes = [j for j, y in enumerate(nums) if y == nextWord]
	# 		for idx in nextIndexes:
	# 			print(words[idx])
	# 	length -= 1
# End redo


	# while length > 0:
	# 	word = ""
	# 	#result = ""
	# 	wordLen = 0
	# 	for c in range(0, length):
	# 		word += cipherNum[c] + " "
	# 		wordLen += 1

	# 	indexes = [i for i, x in enumerate(nums) if x == word]
		
	# 	cpyLen = length
	# 	for index in indexes:
	# 		nextWord = ""
	# 		for d in range(length, len(cipherNum)):
	# 			nextWord += cipherNum[d] + " "
	# 		result = words[index] + " "
	# 		#print(words[index])
	# 		prevResult = result
	# 		nextIndexes = [j for j, y in enumerate(nums) if y == nextWord]
	# 		for idx in nextIndexes:
	# 			result = previousResult
	# 			result += words[idx]
	# 			print(result)
	# 		cpyLen -= 1
	# 	length -= 1
				
	# for item in found:
	# 	print(item)

	# length = len(cipherNum)
	# for item in found:
	# 	word = ""
	# 	for c in range(len(item), length):
	# 		word += cipherNum[c] + " "
	# 		#print(word)
	# 	if word in nums:
	# 		print(item + " " + word)


	# wordNumFile.close()
	# numFile.close()




# 	# If not a shift cipher, try frequency analysis 

# 	total = 0
# 	alphaFreq = {"a":0, "b":0, "c":0, "d": 0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0,
# 		"w":0, "x":0, "y":0, "z":0}  # How many times each letter occurs

# 	alphaMap = {"a": "", "b":"", "c":"", "d":"", "e":"", "f":"", "g":"", "h":"", "i":"", "j":"", "k":"", "l":"", "m":"", "n":"", "o":"", "p":"", "q":"", 
# 		"r":"", "s":"", "t":"", "u":"", "v":"", "w":"", "x":"", "y":"", "z":""}  #Mapping of all letters

# 	# alphaMap = {"a": "a", "b":"b", "c":"c", "d":"d", "e":"e", "f":"f", "g":"g", "h":"h", "i":"i", "j":"j", "k":"k", "l":"l", "m":"m", "n":"n", "o":"o", "p":"p", "q":"q", 
# 	# 	"r":"r", "s":"s", "t":"t", "u":"u", "v":"v", "w":"w", "x":"x", "y":"y", "z":"z"}  #Mapping of all letters

# 	for char in cArray:
# 		if char == " ":
# 			cArray.remove(char)  # Remove whitespace
# 		else:
# 			for a in alphaFreq:
# 				if a == char:
# 					alphaFreq[a] = alphaFreq[a] + 1 # Count how many times each letter appears
# 					total += 1

# 	#print(alphaDict)
	

# 	for letter in alphaFreq:
# 		if alphaFreq[letter] == 0:  # Remove all letters that don't appear
# 			del alphaMap[letter]

# 	# Find double letters
# 	commonDoubles = ['l', 's', 'e', 'f', 'o', 'm', 't', 'z', 'n', 'i', 'r', 'd', 'g', 'b']
# 	#lastLetter = cArray[0]
# 	doubles = []
	
# 	for char in range(1, len(cArray)):
# 		doubleIdx = 0
# 		lastLetter = cArray[char]
# 		if cArray[char] == cArray[char - 1]:  # check pairs of strings for double letters
# 			if lastLetter not in doubles:
# 				#print("Double letter: " + cArray[char] + cArray[char-1])
# 				doubles.append(lastLetter)
# 				if lastLetter == commonDoubles[0]:
# 					doubleIdx += 1
# 				alphaMap[lastLetter] = commonDoubles[doubleIdx] #map last letter to next common double
# 				commonDoubles.remove(commonDoubles[doubleIdx])
# 				common = common.replace(commonDoubles[doubleIdx], "")


# # #Revert to this if messed up
# # 	length = len(common)
# # 	for i in range(0, length):  # Maps the 12 most frequently appearing letters to the 12 most frequent letters in English lang
# # 		if alphaMap[cArray[i]] == "":
# # 			mostCommon = max(copy.items(), key=operator.itemgetter(1))[0]  # finds most commonly occuring letter
# # 			if copy[mostCommon] == 0:  # break once we reach letters that don't appear in the encrypted string since they don't have to be mapped
# # 				break
# # 			copy[mostCommon] = 0  # Sets most common letter frequency to 0 to find next most common
# # 			alphaMap[mostCommon] = common[0]
# # 			common = common.replace(common[0],"")

# 	copy = alphaFreq
# 	for i in range(0, len(cArray)):  # Maps the 12 most frequently appearing letters to the 12 most frequent letters in English lang
# 		mostCommon = max(copy.items(), key=operator.itemgetter(1))[0]  # finds most commonly occuring letter
# 		if copy[mostCommon] == 0:  # break once we reach letters that don't appear in the encrypted string since they don't have to be mapped
# 			break
# 		copy[mostCommon] = 0  # Sets most common letter frequency to 0 to find next most common
# 		if alphaMap[mostCommon] == "":

# 			if alphaMap[mostCommon] == common[0]:
# 				alphaMap[mostCommon] = common[1]
# 				common = common.replace(common[1], "")
# 			else:
# 				alphaMap[mostCommon] = common[0]
# 				common = common.replace(common[0], "")

# 			# or

# 			# alphaMap[mostCommon] = common[0]
# 			# common = common.replace(common[0], "")


# 	#Find unmapped letters
# 	print("common = " + common)
# 	unmapped = []
# 	for char in alphaMap:
# 		if alphaMap[char] == "":
# 			alphaMap[char] = "."#common[0]
# 			#common = common.replace(common[0], "")
# 	result = ""
# 	for char in cArray:
# 		result += alphaMap[char]
# 		#print(alphaMap[char])
# 	print("".join(cArray))
# 	print(result + "\n")




if __name__ == '__main__':
	key = "fpaijnewxtslkdyqzmhrgovbcu"  # Encryption key
	print(convertToNum("ejitpspawaqlejitaiulrtwllrflrllaoatwsqqjatgackthlsiraoatwlplqjatwjufrhlhutsqataqitatsaittkstqfjcae"))

	#decrypt("fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc")  # whatsinanamearosebyanyothernamewouldsmellassweet

	#decrypt("oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy")  # therearetwothingstoaimatinlifefirsttogetwhatyouwantandafterthattoenjoyitonlythewisestofmankindachievethesecond
	# # print("\n\n")

	decrypt("ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae")

		# Most common = a; patterns: awa, aoa, ata, atsa, atga
	# print("\n\n")

	# decrypt("iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe")
	# 	+ "sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna"
	# 	+ "hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn"
	# 	+ "bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz")


	# encrypt("He who fights with monsters should look to it that he himself does not become a monster. And if you"
	# 	+ "gaze long into an abyss, the abyss also gazes into you", key)

	# encrypt("There is a theory which states that if ever anybody discovers exactly what the Universe is for and why"
	# 	+ "it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable."
	# 	+ "There is another theory which states that this has already happened.", key)

	done = input(" ")
	if len(done) >= 0:
		pass

