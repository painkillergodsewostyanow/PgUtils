class LinkedListObj:
    def __init__(self, data=None):
        self.data = data
        self.__next = None
        self.__prev = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def __check_and_actions_if_first_add(self, obj):
        if self.__length == 0:
            self.__head = obj
            self.__tail = obj
            self.__length += 1
            return True
        return False

    def __check_and_actions_if_last_del(self):
        if self.__length == 1:
            self.__head = None
            self.__tail = None
            self.__length -= 1
            return True
        return False

    def __get_by_index(self, index):
        count = 0
        h = self.__head
        while h and count != index:
            h = h.__next
            count += 1
        return h

    def __get_by_slice(self, item):
        result = LinkedList()
        count = item.start
        obj = self.__get_by_index(count)
        while obj and count < item.stop:
            result.push_back(self.__get_by_index(count).data)
            count += item.step

        return result

    def __check_index(self, item):
        if not 0 <= item < self.__length:
            raise IndexError('index out of range')

    def __check_slice(self, item):
        if not (0 <= item.start < self.__length):
            raise IndexError("Start")
        if item.stop < item.start or item.stop > self.__length:
            raise IndexError("Stop")

    def push_back(self, data):
        obj = LinkedListObj(data)

        if self.__check_and_actions_if_first_add(obj):
            return

        self.__tail.__next = obj
        obj.__prev = self.__tail
        self.__tail = obj

        self.__length += 1
        return

    def push_front(self, data):
        obj = LinkedListObj(data)

        if self.__check_and_actions_if_first_add(obj):
            return

        self.__head.prev = obj
        obj.__next = self.__head
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

        obj = self.__tail.__prev
        obj.__next = None
        self.__tail = obj
        self.__length -= 1

        return obj

    def pop_front(self):
        if self.__check_and_actions_if_last_del():
            return

        obj = self.__head.next
        obj.__prev = None
        self.__head = obj
        self.__length -= 1

        return obj

    def __getitem__(self, item):
        result = None

        if isinstance(item, int):
            self.__check_index(item)
            result = self.__get_by_index(item).data

        # TODO: add slice
        if isinstance(item, slice):
            if not item.start:
                item = slice(0, item.stop, item.step)

            if not item.stop:
                item = slice(item.start, self.__length, item.step)

            if not item.step:
                item = slice(item.start, item.stop, 1)

            self.__check_slice(item)
            result = self.__get_by_slice(item)

        return result

    def __setitem__(self, key, value):
        # TODO: add slice
        if isinstance(key, int):
            self.__check_index(key)
            self.__get_by_index(key).data = value

        return

    def __str__(self):
        result = ""
        for i in range(self.__length):
            result += f" <-{self.__get_by_index(i).data}-> "
        if result:
            return f"None {result} None"
        return "None"

    def __len__(self):
        return self.__length


lst = LinkedList()
lst.push_front(0)
lst.push_back(1)
lst.push_back(2)
lst.push_back(3)
lst.push_back(4)
lst.push_back(5)
lst.push_back(6)
lst.push_back(7)
lst.push_back(8)
lst.push_back(9)
lst.push_back(10)

print(lst[::])
print(lst[:11])
print(lst[0:])
print(lst[::3])

