from Tree import Node



class BinTree:
    root: Node
    __ix_left = 0
    __ix_right = 1

    def __inti__(self):
        self.root = None

    def __iadd__(self, val):
        if root is None:
            self.root = Node
        else:
            walker = root
            while walker != None:
                if walker.data < val:
                    # go left 
                    walker = walker.children[self.__ix_left]
                else:
                    walker = walker.children[self.__ix_right]
            

        return self

    


if __name__ == "__main__":
    root = Node("hello")
    val = 0b10001
    mask = 0b100000
    print(f"val: {val:b}")
    val = val << 1
    t  = val & 0b100000
    print(f"val: {val:b}")
    print(f"mak: {t:b}")
    val -= mask
    val |= 0b000001
    print(f"val: {val:b}")
