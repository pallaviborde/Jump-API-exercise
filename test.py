import nose
from .images import Resource
from nose.tools import *
class TestFruit(object):
    # Function to test if the passed value of first name exists or not
    
	def test_search(self):
		self.resource = Resource()
		result = Resource.search_res("Neena")
		if result == True:
			nose.tools.assert_true(result)
		else:
			nose.tools.assert_false(result)

	
nose.main()
    


