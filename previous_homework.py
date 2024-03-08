import datetime


class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.current_value = 0
        self.result_list = []

    def __iter__(self):
        self.current_value -= 1
        for list in self.list_of_lists:
            for item in list:
                self.result_list.append(item)
        return self

    def __next__(self):
        self.current_value += 1
        if self.current_value < len(self.result_list):
            return self.result_list[self.current_value]
        else:
            raise StopIteration


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            text = open(path, 'a+')
            result = old_function(*args, **kwargs)
            text.write(f"Вызвана функция {old_function.__name__} c аргументами {args} и {kwargs}\n"
                       f"в {datetime.datetime.now()}\n c результатом {result}\n")
            return result

        return new_function

    return __logger


path = 'file.log'


@logger(path)
def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
