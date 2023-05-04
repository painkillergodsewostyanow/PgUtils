class LinkedListObj:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __check_and_actions_if_first_add(self, obj):
        if self.tail is None:
            if self.head is None:
                self.head = obj
                self.tail = obj
                self.length += 1
                return True

    def __check_and_actions_if_first_del(self):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        return True

    def __get_by_index(self, index):
        h = self.head
        count = 0
        while h and count != index:
            h = h.next
            count += 1
        return h

    def __check_index(self, item):
        # TODO: add check slice
        if type(item) == int:
            if not 0 <= item < self.length:
                raise IndexError('index out of range')

    def push_back(self, data):
        obj = LinkedListObj(data)

        if self.__check_and_actions_if_first_add(obj):
            return

        self.tail.next = obj
        obj.prev = self.tail
        self.tail = obj

        self.length += 1
        return

    def push_front(self, data):
        obj = LinkedListObj(data)

        if self.__check_and_actions_if_first_add(obj):
            return

        self.head.prev = obj
        obj.next = self.head
        self.head = obj

        self.length += 1
        return

    def last(self):
        return self.tail

    def first(self):
        return self.head

    def pop_back(self):
        if self.__check_and_actions_if_first_del():
            return

        obj = self.tail.prev
        obj.next = None
        self.tail = obj
        self.length -= 1

        return obj

    def pop_front(self):
        if self.__check_and_actions_if_first_del():
            return

        obj = self.head.next
        obj.prev = None
        self.head = obj
        self.length -= 1

        return obj

    def __getitem__(self, item):
        # TODO: add slice

        self.__check_index(item)

        return self.__get_by_index(item)

    def __setitem__(self, key, value):
        # TODO: add slice

        self.__check_index(key)

        self.__get_by_index(key).data = value

        return

    def __str__(self):
        # TODO: norm str map
        h = self.head
        while h:
            print(h.data)
            h = h.next
        return "test"

    def __len__(self):
        return self.length





