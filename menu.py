def outputMenu(menuData):
	for currEntryAlias in menuData:
		currEntry = menuData[currEntryAlias]
		currEntryName = currEntry[0]
		currEntryValue = currEntry[1]
		print "\t", currEntryName, "-", currEntryValue
	print "Type the chararacters shown in square brackets:",

def getSelectionAttempt(menuRequest, menuData):
	print menuRequest
	outputMenu(menuData)
	return raw_input()

def getSelection(menuRequest, menuData, maxTries=3):
	for i in range(maxTries):
		try:
			selection = getSelectionAttempt(menuRequest, menuData)
			break
		except KeyError:
			print "You did not select a valid option"
	return menuData[selection.lower()][1]

