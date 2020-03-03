from hashtable import Hashtable

class HashSet(object):

	def __init__(self, items=None):
		'''Initialize this set as a Hashtable and adds items if any'''
		self.hash = Hashtable()	# Set is a hashtable
		self.size = 0 # Number of elements
		# Adds the given items
		if items is not None:
			for item in items:
				self.add(item)


	# Adds given item is not found in set
	def add(self, item):
		pass

	# Returns true if item is found in set
	def contains(self, item):
		pass

	# Removes items if not found in set
	def remove(self,item):
		pass

	# Returns a new set that contains all elements from both sets
	def union(self, set):
		pass

	# Returns a new set that contains the common items in both sets
	def intersection(self, set):
		pass

	# Returns a new set that contains the different elements in both sets
	def difference(self, set):
		pass

	# Returns True if set is found in given set
	def is_subset(self,set):
		pass



def test_hash_set():
	pass



if __name__ == '__main__':
	test_hash_set()