
from set import HashSet
import unittest

class SetTest(unittest.TestCase):

	def test_init(self):
		data = ["Mondale", "is", "great"]
		h = HashSet(data)
		assert h.size == 3

	def test_add(self):
		h = HashSet()
		assert h.size == 0
		h.add("Mondale")
		assert h.size == 1

	def test_contains(self):
		h = HashSet()
		h.add("Mondale")
		assert h.contains("Mondale") == True
		assert h.contains("Alfred") == False


	def test_remove(self):
		h = HashSet()
		h.add("Egg")
		h.add("Tuna")
		h.remove("Egg")
		assert h.size == 1


	def test_union(self):

		set_one = HashSet(["A", "B", "C"])
		set_two = HashSet(["C", "D", "E"])

		set_three = set_one.union(set_two)

		assert set_three.size == 5


	def test_intersection(self):

		set_one = HashSet(["A", "B", "C"])
		set_two = HashSet(["C", "D", "E"])

		set_three = set_one.intersection(set_two)

		assert set_three.contains("C") == True
		assert set_three.size == 1

	def test_difference(self):
		set_one = HashSet(["A", "B", "C"])
		set_two = HashSet(["C", "D", "E"])

		set_three = set_one.difference(set_two)

		assert set_three.size == 4



	def test_is_subset(self):

		set_one = HashSet(["A", "B", "C"])
		set_two = HashSet(["C", "D", "E"])

		assert set_one.is_subset(set_two) == False
		assert set_one.is_subset(HashSet(["A", "B", "C"])) == True
		assert set_one.is_subset(HashSet(["A", "B", "C", "D"])) == True


















