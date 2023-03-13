class Birds:
	def __init__(self):
		self.members  = ["Eagle", "Owls"]

	def printMembers(self):
		print('Printing members of the Birds class')
		for member in self.members:
			print('\t%s ' % member)
