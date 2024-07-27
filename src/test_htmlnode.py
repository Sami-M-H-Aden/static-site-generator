import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    node=HTMLNode()
    node_2=HTMLNode("p")
    node_3=HTMLNode("p","waaaa")
    node_4=HTMLNode("p","waaaa",[])
    node_5=HTMLNode("p","waaaa",[],{})
    def check_exception(self):
        global node,node_2,node_3,node_4,node_5
        self.assertRaises(NotImplementedError(),node.to_html())
    def is_eq(self):
        global node,node_2,node_3,node_4,node_5
        self.assertEqual(node_2.props_to_html(),"HTMLNode(p,waaaa,[],{})")
    def is_none(self):
        global node,node_2,node_3,node_4,node_5
        self.assertIsNotNone(node_3.tag)
    def is_not_none(self):
        global node,node_2,node_3,node_4,node_5
        self.assertIsNone(node_3.tag)





if __name__ == "__main__":
    unittest.main()