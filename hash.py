'''
size of table = 200
'''


class HashTable:
    '''
    class of hash tables
    '''
    def __init__(self):
        self.size = 200
        self._table = [[0] for i in range(self.size)]
        self._number = 0
        self._cursor_i = -1
        self._cursor_j = -1

    def add(self, element):
        '''
        add a new element to hash table
        '''
        index = hash(element) % self.size
        if element not in self._table[index]:
            self._table[index].append(element)
            self._number += 1
        else:
            pass

    def remove(self, element):
        '''
        delete element from hash table
        '''
        index = hash(element) % self.size
        try:
            self._table[index].remove(element)
            self._number -= 1
            return self
        except ValueError:
            return self

    def __repr__(self):
        return str(self._table)

    def __len__(self):
        return self._number

    def __contains__(self, element):
        return element in self._table[hash(element) % self.size]

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor_i + 1 >= len(self._table):
            if self._cursor_j + 1 >= len(self._table[self._cursor_j]):
                self._cursor_i = -1
                self._cursor_j = -1
                raise StopIteration()
        elif self._cursor_i == -1:
            self._cursor_i += 1
        elif self._cursor_j + 1 >= len(self._table[self._cursor_i]):
            if self._cursor_i + 1 <= len(self._table):
                self._cursor_i += 1
                self._cursor_j = 0
                return self._table[self._cursor_i][self._cursor_j]
        self._cursor_j += 1
        return self._table[self._cursor_i][self._cursor_j]

TABLE = HashTable()
TABLE.add('Аннушка')
TABLE.add('wertyuio')
TABLE.add('help me pls')
# print(len(TABLE))
# print('Аннушка' in TABLE)
# print('Аннушка' not in TABLE)
for i, elem in enumerate(TABLE, start=0):
    # print(elem)
    pass
# TABLE.add('Аннушка')
# print(TABLE)
# TABLE.remove('Аннушка')
# TABLE.remove('Аннушка')
# print(TABLE)
