class Node:
    # parent: Node
    def __init__(self, data, parant = None):
        self.data = data
        self.parant = parant
        self.children = []

    def __iadd__(self, child):
        self.children.append(child)
        child.parant = self
        return self

    def __len__(self):
        return len(self.children)

    def __str__(self):
        return f"* {str(self.data)}:\n\t{str([str(n.data) for n in self.children])}"
    
    def __repr__(self):
        return f"{self.data}:{len(self)}"


    def __iter__(self):
        for l in self.get_left():
            yield from l
        yield self
        for r in self.get_right():
            yield from r
        
        # raise StopIteration()

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
        


if __name__ == "__main__":
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
