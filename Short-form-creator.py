def initials(phrase):
	words = phrase.split()
	result = ""

	for word in words:
		result += word[0]
	return result.upper()


print(initials("Universal Serial Bus")) # Should be: USB
