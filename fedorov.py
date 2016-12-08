import time


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return 'value = {0}; next = {1}'.format(self.value, self.next)


class SinglyLinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None
        
        self._MAXIMUM = None

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

    def get_max(self, node, f=False):
        """
        Получить максимальное значение
        node : элемент
        f    : если элемент первый
        """
        max_node = node
        prev = None
        while node.next:                          # проходим циклом по элементам, со второго элемента
            if max_node.value < node.next.value:  # в первой итерации сравниваем первый элемент со вторым,
                                                  # далее максимальный со следующими
                if f:                             # если элемент первый, т.е. начало сортировки
                    self._MAXIMUM = node.next     # фиксируем максимальный элемент, чтобы иметь ссылку (если у
                                                  # какого-либо элемента не будет предыдущего элемента,
                                                  # то предыдущим станет максимальный)
                max_node = node.next
                prev = node
            node = node.next
        if not prev:                              # если нет предыдущего, то предыдущим станет максимальный
            prev = self._MAXIMUM                  # это случится если переданный в функцию элемент окажется максимальным
        return prev, max_node

    def change_links(self, previos_node, max_node):
        """
        Переместить ссылки
        previos_node : предыдущий элемент
        max_node     : максимальн элемент итерации
        """
        previos_node.next = max_node.next         # предыдущий ссылается на следующий после максимального
        max_node.next = self.first                # максимальный ссылается на первый
        self.first = max_node                     # максимальный становится первым

    def sort_2(self):
        """
        Функция сортировки односвязного списка
        """
        previos_node = None                       # установка для первой итерации
        current = self.first                      # установка для первой итерации

        f = True  # если первая итерация (с помощью флага фиксируем самый большой элемент)
        while current:
            previos_node, max_node = self.get_max(current, f)
            f = False
            if max_node == self.first:                                #   curr
                                                                      # |  e1  |e2|e3|e4|e5|
                                                                      #   max
                previos_node = current
                current = current.next

                                                                      #      curr
                                                                      # |e1|  e2  |e3|  e4  |e5|
                                                                      #                max

            elif max_node == current:                                 #         curr
                                                                      # |e4|e1|  e2  |e3|e5|
                                                                      #         max
                current = current.next
                self.change_links(previos_node, max_node)
                #previos_node = current
                #current = current.next
            else:                                                     #            curr
                self.change_links(previos_node, max_node)             # |e2|e4|e1|  e3  |e5|
                                                                      # ...
            # В последней итерации ссылка на максимальный элемент уничтожаестя, т.к. previos_node.next = max_node.next
            # в функции change_links, т.к. previos_node = _MAXIMUM, а max_node.next = None



