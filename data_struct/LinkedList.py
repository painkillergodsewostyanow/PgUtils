class LinkedListObj:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def __check_and_actions_if_first_add(self, obj):
        if self.__tail is None:
            if self.__head is None:
                self.__head = obj
                self.__tail = obj
                self.__length += 1
                return True

    def __check_and_actions_if_last_del(self):
        if self.__length == 1:
            self.__head = None
            self.__tail = None
            self.__length -= 1
            return True
        return

    def __get_by_index(self, index):
        h = self.__head
        count = 0
        while h and count != index:
            h = h.next
            count += 1
        return h

    def __check_index(self, item):
        # TODO: add check slice
        if type(item) == int:
            if not 0 <= item < self.__length:
                raise IndexError('index out of range')

    def push_back(self, data):
        obj = LinkedListObj(data)

        if self.__check_and_actions_if_first_add(obj):
            return

        self.__tail.next = obj
        obj.prev = self.__tail
        self.__tail = obj

        self.__length += 1
        return

    def push_front(self, data):
        obj = LinkedListObj(data)

        if self.__check_and_actions_if_first_add(obj):
            return

        self.__head.prev = obj
        obj.next = self.__head
        self.__head = obj

        self.__length += 1
        return

    @property
    def last(self):
        return self.__tail.data

    @last.setter
    def last(self, value):
        self.__tail.data = value

    @property
    def first(self):
        return self.__head.data

    @first.setter
    def first(self, value):
        self.__head.data = value

    def pop_back(self):
        if self.__check_and_actions_if_last_del():
            return

        obj = self.__tail.prev
        obj.next = None
        self.__tail = obj
        self.__length -= 1

        return obj

    def pop_front(self):
        if self.__check_and_actions_if_last_del():
            return

        obj = self.__head.next
        obj.prev = None
        self.__head = obj
        self.__length -= 1

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
        result = ""
        for i in range(self.__length):
            result += f" <-{self[i].data}-> "
        if result:
            return f"None {result} None"
        return "None"

    def __len__(self):
        return self.__length


lst = LinkedList()
lst.push_front(123)
lst.push_back(456)
lst.push_back(789)
lst.pop_front()
lst.pop_back()
lst.pop_front()
print(lst)

