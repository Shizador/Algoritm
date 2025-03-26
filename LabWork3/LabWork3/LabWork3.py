# -*- coding: cp1251 -*-
import random
from queue import Queue

class TreeNode:
    def __init__(self, value):
        self.v = value
        self.l = None  # левый узел
        self.r = None  # правый узел

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.v:
            if node.l is None:
                node.l = TreeNode(value)
            else:
                self._add_recursive(node.l, value)
        else:
            if node.r is None:
                node.r = TreeNode(value)
            else:
                self._add_recursive(node.r, value)

    def find(self, val):
        '''
        Поиск узла.
        Если узел не пуст, вызываем вспомогательную функцию поиска,
        иначе возвращаем None.
        '''
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        '''
        Вспомогательная рекурсивная функция поиска.
        Если узел найден, возвращаем его. Если значение узла больше искомого,
        продолжаем поиск в левом поддереве, если оно не пустое. Если значение
        узла меньше искомого, продолжаем поиск в правом поддереве,
        если оно не пустое.
        '''
        if val == node.v:
            return node.v
        elif (val < node.v and node.l != None):
            return self._find(val, node.l)
        elif (val > node.v and node.r != None):
            return self._find(val, node.r)

    def deleteTree(self):
        '''
        Удаление дерева.
        Удаляем корень, все остальное делает сборщик мусора.
        '''
        self.root = None
    def printTree(self):

        if self.root is not None:
            print("Дерево:")
            self._printTree(self.root)
            print()
        else:
            print("Дерево не существует")

    def _printTree(self, node):
        '''
        Вспомогательная рекурсивная функция печати.
        '''
        if node is not None:
            print(str(node.v), end=' ')
            self._printTree(node.l)
            self._printTree(node.r)

    def BFS(self):
        '''
        Обход дерева в ширину.
        '''
        if self.root is not None:
            q = Queue()
            q.put(self.root)
            while not q.empty():
                x = q.get()
                print(str(x.v), end=' ')
                if x.l is not None:
                     q.put(x.l)
                if x.r is not None:
                     q.put(x.r)
            print()
        else:
            print("Дерево не существует")

    def countNodes(self):
        '''
        Метод для подсчета количества узлов в бинарном дереве поиска.
        Вызываем вспомогательную функцию для рекурсивного подсчета.
        '''
        return self._countNodes(self.root)

    def _countNodes(self, node):
        '''
        Вспомогательная рекурсивная функция для подсчета узлов.
        Если узел пустой, возвращаем 0. Иначе, считаем корень + количество узлов
        в левом и правом поддеревьях.
        '''
        if node is None:
            return 0
        return 1 + self._countNodes(node.l) + self._countNodes(node.r)

    def countLeaves(self):
        '''
        Метод для подсчета количества листьев в бинарном дереве поиска.
        Вызываем вспомогательную функцию для рекурсивного подсчета.
        '''
        return self._countLeaves(self.root)

    def _countLeaves(self, node):
        '''
        Вспомогательная рекурсивная функция для подсчета листьев.
        Если узел пустой, возвращаем 0. Если узел является листом, 
        возвращаем 1. В противном случае, считаем листья в левом и правом поддеревьях.
        '''
        if node is None:
            return 0
        if node.l is None and node.r is None:
            return 1
        return self._countLeaves(node.l) + self._countLeaves(node.r)

    def height(self):
    
        return self._height(self.root)

    def _height(self, node):
   
        if node is None:
            return -1
        left_height = self._height(node.l)
        right_height = self._height(node.r)
        return 1 + max(left_height, right_height)

    def depth_first_traversal(self):

        if self.root is None:
            return []

        stack = []
        result = []
        stack.append(self.root)

        while stack:
            node = stack.pop()
            result.append(node.v)

            # Добавляем правый узел в стек, чтобы сначала обработать левый
            if node.r is not None:
                stack.append(node.r)
            if node.l is not None:
                stack.append(node.l)

        return result

    def breadth_first_traversal(self):
        if self.root is None:
            return []

        queue = [self.root]
        result = []

        while queue:
            current_level = []
            next_level = []

            for node in queue:
                current_level.append(node.v)
                if node.l:
                    next_level.append(node.l)
                if node.r:
                    next_level.append(node.r)

            result.append(current_level)
            queue = next_level

        return result

    def pretty_print(self):
        levels = self.breadth_first_traversal()
        max_width = len("  ".join(str(x) for x in levels[-1]))

        for level in levels:
            level_str = "  ".join(str(x) for x in level).center(max_width)
            print(level_str)

# Пример использования
min_val = 1
max_val = 100
n = 10

random_numbers = random.sample(range(min_val, max_val + 1), n)
print("Сгенерированные числа:", random_numbers)

tree = Tree()
tree.add(random_numbers[0])
for num in random_numbers[1:]:
    tree.add(num)

tree.printTree()
print("Количество узлов в дереве:", tree.countNodes())
print("Количество листьев в дереве:", tree.countLeaves())
print("Высота дерева:", tree.height())
print("Обход в глубину:", tree.depth_first_traversal())
nodes = [15, 10, 20, 8, 12, 17, 25]
for node in nodes:
    tree.add(node)
print("Красивый вывод бинарного дерева:")
tree.pretty_print()