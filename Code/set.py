from hashtable import HashTable

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
		self.hash[item] = True
		self.size += 1


	# Returns true if item is found in set
	def contains(self, item):
		return item in self.hash

	# Removes items if found in set
	def remove(self,item):
		if self.contains(item):
			self.hash.pop(item)
			self.size -= 1


	# Returns a new set that contains all elements from both sets
	def union(self, other_set):
		new_hash_set = HashSet()

		for item in self.hash:
			new_hash_set.add(item)


		for item in other_set:
			new_hash_set.add(item)
			
		return new_hash_set

	# Returns a new set that contains the common items in both sets
	def intersection(self, other_set):
		new_hash_set = HashSet()
		
		for item in other_set:
			if item in self.hash:
				new_hash_set.add(item)



	# Returns a new set that contains the different elements in both sets
	def difference(self, other_set):
		new_hash_set = HashSet()

		for item in self.hash:
			if other_set.contains(item) == False:
				new_hash_set.add(item)

	# Returns True if set is found in given set
	def is_subset(self,other_set):
	
		for item in self.hash:
			if other_set.contains(item) == False:
				return False

		return True



def test_hash_set():
	print("testing")



if __name__ == '__main__':
	test_hash_set()