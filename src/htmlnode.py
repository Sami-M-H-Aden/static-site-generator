class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    def props_to_html(self):
        if not isinstance(self.props,dict):
            return ""
        changed_html=""
        for key in self.props:
            changed_html+=f"{key}={self.props[key]} "
        return changed_html
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"
    
