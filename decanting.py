import search


class Decant(search.Nodes):

    def start(self):
        return {'f1': 5,
                'f2': 3,
                'f3': 0}

    def goal(self, node):
        return [node[i] for i in node] == [4, 0, 4]

    # This method will give the capacity of the particular vessel
    def chk_capacity(self, key):
        if key == 'f1':
            return 5
        if key == 'f2':
            return 3
        if key == 'f3':
            return 8

    # This method is doing 1 legal move. and
    # Return the updated node to the algorithm.
    def move(self, ind, node):
        j = ind + 2
        if ind == len(node) - 1:
            ind = -1
            # print(ind)
            j = ind + 1
        if ind == len(node) - 2:
            j = 0
        if list((node.values()))[ind + 1] < self.chk_capacity(list(node)[ind + 1]):
            # print("true1")
            while 1:
                if list((node.values()))[ind] == 0 or \
                        list((node.values()))[ind + 1] == self.chk_capacity(list(node)[ind + 1]):
                    break

                node[list(node)[ind]] = list((node.values()))[ind] - 1
                node[list(node)[ind + 1]] = list((node.values()))[ind + 1] + 1
        # print(node.values())
        else:
            if list((node.values()))[j] < self.chk_capacity(list(node)[j]):
                while 1:
                    if list((node.values()))[ind] == 0 or \
                            list((node.values()))[j] == self.chk_capacity(list(node)[j]):
                        break
                    node[list(node)[ind]] = list((node.values()))[ind] - 1
                    node[list(node)[j]] = list((node.values()))[j] + 1
                # print(node.values())b
        return node

    def succ(self, node):
        index = []
        for flask in list(node.keys()):
            index.append(list(node.keys()).index(flask))

        for i in index:
            new_node = node.copy()
            if list(new_node.values())[i]:
                new_node = self.move(i, new_node)
                # print("new: ", new_node)
                yield new_node
            else:
                continue
