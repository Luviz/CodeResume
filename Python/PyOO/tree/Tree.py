class Node:
    # parent: Node
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = parent
        self.children = []

    def __iadd__(self, child):
        self.children.append(child)
        child.parent = self
        return self

    def __len__(self):
        return len(self.children)

    def __str__(self):
        if len(self) > 0:
            return f"* {str(self.data)}:\n\t{str([str(n.data) for n in self.children])}"
        else:
            return f"* {str(self.data)}"
    
    def __repr__(self):
        return f"{self.data}:{len(self)}"


    def __iter__(self):
        for l in self.get_left():
            yield from l
        yield self
        for r in self.get_right():
            yield from r
        
    def get_list(self):
        res = []
        l = self.get_left()
        res.extend([v.get_list() for v in l])
        res.append(self)
        r = self.get_right()
        res.extend([v.get_list() for v in r])
        return res
    
    def get_left(self, pivot=1):
        return self.children[:pivot]

    def get_right(self, pivot=1):
        return self.children[pivot:]

    def GetPath(self):
        # path.append(self.data)
        if self.parent == None:
            return [self]
        path = self.parent.GetPath()
        path.append(self)
        return path
        

def __test_basic_iter():
    ## TEST
    root = Node("root")
    a = Node("Alpha")
    b = Node("Beta")
    c = Node("Gamma")
    root += a
    root += b
    a += c
    # print(dir(root))
    print(str(root))
    for n in root.children:
        print(n)

    print(root.get_list())

    for n in root:
        print(n)

    print(c.GetPath())

def __test_large_scale():
    alphabet = [chr(v) for v in range(ord('A'), ord('Z')+1)]
    root = Node('root')
    for char in alphabet[:5]:
        root += Node(char)

    for char in alphabet[5:10]:
        root.children[0] += Node(char)

    for char in alphabet[10:15]:
        root.children[1] += Node(char)

    for char in alphabet[15:20]:
        root.children[2] += Node(char)

    for char in alphabet[20:]:
        root.children[3] += Node(char)

    print(root.get_list())
    for n in root: 
        print(n, n.GetPath())
    print()
    print(root.children[2].children[1].GetPath())

if __name__ == "__main__":
    # __test_basic_iter()
    __test_large_scale()