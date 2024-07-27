import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a  node", "bold")
        self.assertNotEqual(node, node2)
    def test_eq_2(self):
        node = TextNode("This is a text node", "bold","https:poop")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    def test_is_not_none(self):
        node = TextNode("This is a text node", "bold","https:poop")
        self.assertIsNotNone(node.url)
    def test_is_none(self):
        node2 = TextNode("This is a text node", "bold")
        self.assertIsNone(node2.url)
    def test_is_not_equal(self):
        node = TextNode("This is a text node", "bold","https:poop")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node.text_type,node2.text_type)

if __name__ == "__main__":
    unittest.main()