# import random

class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return "Node: value = {0} next = {1}".format(str(self.value), self.next)


class SinglyLinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' + str(current.value) + '\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def add(self, element):
        if not self.first:
            self.first = self.last = Node(element)
        else:
            self.last.next = self.last = Node(element)

    def push(self, element):
        if not self.first:
            self.first = self.last = Node(element)
        else:
            self.first = Node(element, self.first)

    def insert(self, position, element):
        if not self.first:
            self.first = self.last = Node(element)
            return
        if position == 0:
            self.first = Node(element, self.first)
            return
        current = self.first
        count = 1
        while True:
            if position == count:
                current.next = Node(element, current.next)
                if current.next.next is None:
                    self.last = current.next
                break
            count += 1
            current = current.next

    def len(self):
        length = 0
        if self.first is not None:
            current = self.first
            length += 1
            while current.next:
                current = current.next
                length += 1
        return length

    def sort(self):
        if not self.first or not self.first.next:
            return
        curr = Node(0, None)
        after = Node(0, None)
        before = Node(0, None)
        e = Node(0, None)
        tmp = Node(0, None)

        while (e != self.first.next):
            before = curr = self.first
            after = curr.next

            while curr != e:
                if curr and after:
                    if curr.value > after.value:
                        if curr == self.first:
                            tmp = after.next
                            after.next = curr
                            curr.next = tmp
                            self.first = after
                            before = after
                        else:
                            tmp = after.next
                            after.next = curr
                            curr.next = tmp
                            before.next = after
                            before = after
                    else:
                        before = curr
                        curr = curr.next
                    after = curr.next
                    if after == e:
                        e = curr
                else:
                    e = curr

    def get_max(self, node):
        max_node = node
        while node.next is not None:
            node = node.next
            if max_node.value < node.value:
                max_node = node
        return max_node

    def get_previous_node(self, node):
        current = self.first
        previous_node = None
        while current.next is not None:
            if current == node:
                break
            else:
                previous_node = current
                current = current.next
        return previous_node


    def switch_node_to_first(self, node):
        previous_node = self.get_previous_node(node)
        if previous_node is not None:
            previous_node.next = node.next
            node.next = self.first
            self.first = node


    def sort2(self):
        current = self.first
        while current.next is not None:
            max_node = self.get_max(current)
            if current == max_node:
                current = current.next
            self.switch_node_to_first(max_node)
        self.switch_node_to_first(current)

    def switch3(self, previous, current, next):
        current.next = next.next
        next.next = current
        if previous:
            previous.next = next
        else:
            self.first = next


    def push_max(self, previous, current):
        while True:
            if not current.next or self.sort_max == current.next:
                self.sort_max = current
                break
            else:
                next = current.next
                if current.value > next.value:
                    self.switch3(previous, current, next)
                    current, next = next, current
                previous, current = current, next
                # self.push_max(current, next)


    def sort3(self):
        self.sort_max = None
        while self.sort_max != self.first.next:
            self.push_max(None, self.first)

# N = 50
# instance = SinglyLinkedList()
# for t in random.sample(range(1, N + 1), N):
#     instance.add(t)
# print(instance)
# instance.sort3()
# print(instance)