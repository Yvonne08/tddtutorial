from selenium import webdriver
import unittest

class ToDoApp(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		# She noticed the page title and header meation to-do lists
		self.assertIn('Django', self.browser.title)

if __name__=='__main__':
	unittest.main()