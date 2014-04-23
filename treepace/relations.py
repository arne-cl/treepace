"""Tree node relations."""

import treepace.tree

class Child:
    """A child relation."""
    
    name = "child"
    
    def search(self, node):
        """Return an iterable containing this node's children."""
        return node.children


class Sibling:
    """All siblings (excluding the node itself)."""
    
    name = "sibling"
    
    def search(self, node):
        """Return an iterable containing the siblings of this children."""
        if node.parent:
            return filter(lambda x: x != node, node.parent.children)
        else:
            return []


class NextSibling:
    """An immediately following sibling."""
    
    name = "next_sib"
    
    def search(self, node):
        """Return a list with one element (the next sibling) or an empty
        list."""
        next_index = node.index + 1
        if node.parent and len(node.parent.children) > next_index:
            return [node.parent.children[next_index]]
        else:
            return []
    
    def build(self, context, node):
        """Insert the given node after the context node."""
        context.parent.insert_child(node, context.index + 1)


class Parent:
    """A parent relation."""
    
    name = "parent"
    
    def search(self, node):
        """Return a one-element list with the node's parent or an empty list."""
        return [node.parent] if node.parent else []


class Descendant:
    """A descendant or the node itself."""
    
    name = "desc"
    
    def search(self, node):
        """Return an iterable with all node's descendants in a pre-order
        manner."""
        return treepace.tree.Tree(node).preorder()
