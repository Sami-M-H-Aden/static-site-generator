text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self,TEXT,TEXT_TYPE,URL=None):
        self.text=TEXT
        self.text_type=TEXT_TYPE
        self.url=URL
    
    def __eq__(self,other):
        return (self.text_type == other.text_type
                and self.text == other.text
                and self.url == other.url
                )
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"

