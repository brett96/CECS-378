import operator

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

def tryKeys():
	pass


def decrypt(string):
	cArray = list(string)
	common = "etaoinshrdlucmwfgypbvkjxqz"  #frequent letters in english

	# Tries all possibilities of a shift cipher

	# for char in cArray:
	# 	if char == " ":
	# 		cArray.remove(char)  #Strips whitespace
	# alphabet = "abcdefghijklmnopqrstuvwxyz"
	# for i in range(0, 26):
	# 	for i in range(0, len(cArray)):
	# 		cArray[i] = alphabet[(alphabet.find(cArray[i]) + 1) % 26] # Increments letter by 1
	# 	print("".join(cArray) + "\n\n") # Possible message


	# If not a shift cipher, try frequency analysis 

	total = 0
	alphaFreq = {"a":0, "b":0, "c":0, "d": 0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0,
		"w":0, "x":0, "y":0, "z":0}  # How many times each letter occurs

	alphaMap = {"a": "", "b":"", "c":"", "d":"", "e":"", "f":"", "g":"", "h":"", "i":"", "j":"", "k":"", "l":"", "m":"", "n":"", "o":"", "p":"", "q":"", 
		"r":"", "s":"", "t":"", "u":"", "v":"", "w":"", "x":"", "y":"", "z":""}  #Mapping of all letters

	# alphaMap = {"a": "a", "b":"b", "c":"c", "d":"d", "e":"e", "f":"f", "g":"g", "h":"h", "i":"i", "j":"j", "k":"k", "l":"l", "m":"m", "n":"n", "o":"o", "p":"p", "q":"q", 
	# 	"r":"r", "s":"s", "t":"t", "u":"u", "v":"v", "w":"w", "x":"x", "y":"y", "z":"z"}  #Mapping of all letters

	for char in cArray:
		if char == " ":
			cArray.remove(char)  # Remove whitespace
		else:
			for a in alphaFreq:
				if a == char:
					alphaFreq[a] = alphaFreq[a] + 1 # Count how many times each letter appears
					total += 1

	#print(alphaDict)
	

	for letter in alphaFreq:
		if alphaFreq[letter] == 0:  # Remove all letters that don't appear
			del alphaMap[letter]

	# Find double letters
	commonDoubles = ['l', 's', 'e', 'f', 'o', 'm', 't', 'z', 'n', 'i', 'r', 'd', 'g', 'b']
	#lastLetter = cArray[0]
	doubles = []

	for char in range(1, len(cArray)):
		lastLetter = cArray[char]
		doubleIdx = 0
		if cArray[char] == cArray[char - 1]:  # check pairs of strings for double letters
			if lastLetter not in doubles:
				#print("Double letter: " + cArray[char] + cArray[char-1])
				doubles.append(lastLetter)
				if lastLetter == commonDoubles[0]:
					doubleIdx = 1
				alphaMap[lastLetter] = commonDoubles[doubleIdx] #map last letter to next common double
				#alphaMap[commonDoubles[doubleIdx]] = temp
				#common = common.replace(commonDoubles[doubleIdx], "")
				commonDoubles.remove(commonDoubles[doubleIdx])
				common = common.replace(commonDoubles[doubleIdx], "")


# #Revert to this if messed up
# 	length = len(common)
# 	for i in range(0, length):  # Maps the 12 most frequently appearing letters to the 12 most frequent letters in English lang
# 		if alphaMap[cArray[i]] == "":
# 			mostCommon = max(copy.items(), key=operator.itemgetter(1))[0]  # finds most commonly occuring letter
# 			if copy[mostCommon] == 0:  # break once we reach letters that don't appear in the encrypted string since they don't have to be mapped
# 				break
# 			copy[mostCommon] = 0  # Sets most common letter frequency to 0 to find next most common
# 			alphaMap[mostCommon] = common[0]
# 			common = common.replace(common[0],"")

	copy = alphaFreq
	#for i in range(0, len(cArray)):  # Maps the 12 most frequently appearing letters to the 12 most frequent letters in English lang
	for i in alphaMap:
		mostCommon = max(copy.items(), key=operator.itemgetter(1))[0]  # finds most commonly occuring letter
		if copy[mostCommon] == 0:  # break once we reach letters that don't appear in the encrypted string since they don't have to be mapped
			break
		copy[mostCommon] = 0  # Sets most common letter frequency to 0 to find next most common
		if alphaMap[mostCommon] == "":

			# if alphaMap[mostCommon] == common[0]:
			# 	alphaMap[mostCommon] = common[1]
			# 	common = common.replace(common[1], "")
			# else:
			# 	alphaMap[mostCommon] = common[0]
			# 	common = common.replace(common[0], "")

			# or

			alphaMap[mostCommon] = common[0]
			common = common.replace(common[0], "")


	#Find unmapped letters
	unmapped = []
	for char in alphaMap:
		if alphaMap[char] == "":
			alphaMap[char] = "."#common[0]
			#common = common.replace(common[0], "")
	result = ""
	for char in cArray:
		result += alphaMap[char]
		#print(alphaMap[char])
	print("".join(cArray))
	print(result + "\n")




if __name__ == '__main__':
	key = "fpaijnewxtslkdyqzmhrgovbcu"  # Encryption key

	# decrypt("fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc")  # whatsinanamearosebyanyothernamewouldsmellassweet
	# print("\n\n")

	# decrypt("oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy")  # therearetwothingstoaimatinlifefirsttogetwhatyouwantandafterthattoenjoyitonlythewisestofmankindachievethesecond
	# print("\n\n")

	decrypt("ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae")

		# Most common = a; patterns: awa, aoa, ata, atsa, atga
	# print("\n\n")

	# decrypt("iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe"
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
