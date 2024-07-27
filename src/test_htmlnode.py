import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def is_eq(self):
        node_2=HTMLNode("p")
        self.assertEqual(node_2.props_to_html(),"HTMLNode(p,waaaa,[],{})")
    def is_none(self):
        node_3=HTMLNode("p","waaaa")
        self.assertIsNotNone(node_3.tag)
    def is_not_none(self):
        node_3=HTMLNode("p","waaaa")
        self.assertIsNone(node_3.tag)
if __name__ == "__main__":
    unittest.main()