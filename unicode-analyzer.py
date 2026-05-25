import unicodedata
text = input("Text to analyze: ")
for char in text:
	name = unicodedata.name(char, "UNKNOWN")
	codepoint = hex(ord(char))
	print(f"{char} ------ {codepoint} - {name}")
