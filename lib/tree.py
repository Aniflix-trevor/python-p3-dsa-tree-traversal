class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        def dfs(node):
            if node['id'] == id:
                return node
            for child in node.get('children', []):
                found = dfs(child)
                if found:
                    return found
            return None
        
        if self.root is None:
            return None
        return dfs(self.root)
