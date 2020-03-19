#!/usr/local/bin/python3
class Ordered_Dictionnary:

    def __init__(self, *dic, **param):
        if len(dic) > 1:
            raise ValueError("you can not enter more than a dictionnary at once")
        if len(dic) > 0 and len(param) > 0:
            raise ValueError("you can not enter a dictionnary, plus other parameters")
        self._keys = []
        self._values = []
        self.position = -1
        if len(dic) == 1:
            self.initialize_dic(dic[0])
        else:
            self.initialize_param(param)
    
    def initialize_dic(self, dic):
        for key, value in dic.items():
            self._keys.append(key)
            self._values.append(value)

    def initialize_param(self, param):
        for key, value in param.items():
            self._keys.append(key)
            self._values.append(value)

    def sort(self):
        new_keys = sorted(self._keys)
        new_values = []
        for key in new_keys:
            new_values.append(self.__getitem__(key))
        self._keys = new_keys
        self._values = new_values

    def reverse(self):
        new_keys = sorted(self._keys, reverse=True)
        new_values = []
        for key in new_keys:
            new_values.append(self.__getitem__(key))
        self._keys = new_keys
        self._values = new_values

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        lst = []
        for i, key in enumerate(self._keys):
            lst.append((key, self._values[i]))
        return lst

    def __iter__(self):
        return Iter_Dico(self)

    def __getitem__(self, index):
        if index in self._keys:
            return self._values[self._keys.index(index)]
        elif isinstance(index, int):
            if index > len(self._keys) - 1:
                raise ValueError("Index Error !")
            else:
                return self._keys[index]
        else:
            raise ValueError("there is no key called : {}".format(index))

    def __setitem__(self, index, value):
        if index in self._keys:
            self._values[self._keys.index(index)] = value
        else:
            self._keys.append(index)
            self._values.append(value)

    def __delitem__(self, index):
        if index in self._keys:
            i = self._keys.index(index)
            del self._keys[i]
            del self._values[i]
        else:
            raise ValueError("there is no key called : {}".format(index))

    def __contains__(self, index):
        if index in self._keys:
            return True
        else:
            return False

    def __len__(self):
        return len(self._keys)

    def __add__(self, other):
        for key in other.keys():
            self._keys.append(key)
        for value in other.values():
            self._values.append(value)
        return self

    def __repr__(self):
        empty_str = "{"
        if len(self._keys) > 0:
            for i, key in enumerate(self._keys):
                if i < len(self._keys) - 1:
                    empty_str += "'{}': {}, ".format(key, self._values[i])
                else:
                    empty_str += "'{}': {}".format(key, self._values[i])
        empty_str +="}"
        return empty_str
    
class Iter_Dico:

    def __init__(self, dico):
        self.position = -1
        self._keys = dico._keys

    def __next__(self):
        if self.position == len(self._keys) - 1:
            self.position = 0
            raise StopIteration
        else:
            self.position += 1
            return self._keys[self.position]