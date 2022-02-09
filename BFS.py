
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_data = Node(data)

        if self.root is None:
            self.root = new_data
            return self.root.data
        else:
            currentNode = self.root
            while True:
                #right
                if new_data.data > currentNode.data:
                    if currentNode.right is None:
                        currentNode.right = new_data
                        return self
                    currentNode = currentNode.right

                #left
                elif new_data.data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = new_data
                        return self
                    currentNode = currentNode.left
                else:
                    return print('no duplicates allowed')


    def search(self,data):
        value = Node(data)
        # current = self.root

        if self.root is None:
            return 'empty tree'
        else:
            current = self.root
            try:
                while True:
                    #root
                    if value.data == current.data:
                        return True, current.data
                    #right
                    elif value.data > current.data:
                        if value.data == current.right.data:
                            return True, current.right.data
                        current = current.right
                    #left
                    else:
                        if value.data == current.right.data:
                            return True, current.right.data
                        current = current.left
            except AttributeError:
                return False, 'brak wyników'


    def breadthFirstSearch(self):
        currentNode = self.root
        list = []
        queue = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue[0]
            #print(currentNode.data)
            queue.pop(0)
            list.append(currentNode.data)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        return print(list)

    def breadhtFirstSearchRecursive(self,queue, list):
        if len(queue) == 0:
            return list

        currentNode = queue[0]
        # print(currentNode.data)
        queue.pop(0)
        list.append(currentNode.data)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        return self.breadhtFirstSearchRecursive(queue,list)

tree = BinarySearchTree()

tree.insert(10)
tree.insert(4)
tree.insert(14)
tree.insert(6)
tree.insert(2)
tree.insert(77)
tree.insert(13)
print(tree.search(6))
tree.breadthFirstSearch()
print(tree.breadhtFirstSearchRecursive([tree.root], []))
"""
          10
    4          14
 2      6    13     77
"""