class Tree:
    """
    Управляющий класс дерева (списка). Может добавлять элемент списка, удалять элемент списка, искать по содержимому
    данных списка, и отображать данные всех элементов списка
    """
    first_item = None
    len = 0

    def add_item(self, data):
        """
        Добавить элемент в список.
        :param data: данные элемента
        """
        item = Item(data)
        if not self.first_item:
            self.first_item = item
            return
        last_item = self.first_item
        for x in range(self.len):
            last_item = last_item.next
        item.previous = last_item
        last_item.next = item
        self.len += 1

    def show_items_data(self):
        """
        Вывести данные всех элементов дерева.
        """
        cur_item = self.first_item
        for per in range(self.len+1):
            print(f'{cur_item.data}')
            cur_item = cur_item.next

    def get_item(self, data):
        """
        Получить элемент (объект item) из дерева по совпадению данных
        :param data: данные для поиска
        :return: объект item
        """
        cur_item = self.first_item
        for per in range(self.len):
            if cur_item.data == data:
                return cur_item
            cur_item = cur_item.next

    def get_item_by_index(self, data):
        """
        Получить элемент (объект item) из дерева по совпадению данных
        :param data: данные для поиска
        :return: объект item
        """
        cur_item = self.first_item
        for per in range(data):
            if per == data:
                return cur_item
            cur_item = cur_item.next
        return cur_item

    def del_item(self, data):
        """
        Удаление элемента списка
        :param data: Данные удаляемого элемента
        """
        current = self.get_item(data)
        current.previous.next = current.next
        current.next.previous = current.previous
        self.len -= 1

    def del_item_by_index(self, index):
        """
        Удаление элемента списка
        :param index: Индекс удаляемого элемента
        """
        current = self.get_item_by_index(index)
        current.previous.next = current.next
        current.next.previous = current.previous
        self.len -= 1


class Item:
    """
    Класс элемента списка.
    data: хранит пользовательские данные.
    previous: ссылка на предыдущий элемент списка. None - если отсутствует.
    next: ссылка на следующий элемент списка. None - если отсутствует.
    """
    data = None

    def __init__(self, data, nxt=None, previous=None):
        self.previous = previous
        self.next = nxt
        self.data = data


if __name__ == '__main__':
    #  Создадим и наполним список
    tree = Tree()
    for z in range(1, 6):
        tree.add_item(f'Данные в уровне дерева №{z}')
    #  Примеры использования.
    tree.show_items_data()  # Показать данные всех элементов дерева
    print(10*"*", '\n', tree.get_item("Данные в уровне дерева №2").data, '\n', 10*"*")  # получаем элемент дерева и
    # его данные по данным.
    tree.del_item("Данные в уровне дерева №3")  # удаляем элемент списка
    tree.show_items_data()  # снова выводим элементы списка
    tree.del_item_by_index(2)
    tree.show_items_data()




