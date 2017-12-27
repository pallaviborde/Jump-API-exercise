import nose
from .images import Resource
from nose.tools import *
class TestFruit(object):
	def setup(self):
		self.resource = Resource()
		result = self.resource.search()

	def test_search(self):
		result = []
		result.append(self.resource.search("Neena"))
		if len(result)>0:
			nose.tools.assert_equal(len(result), 1)
		

	
	def teardown(self):
		self.resource.disappear()

nose.main()
    


