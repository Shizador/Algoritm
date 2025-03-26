# -*- coding: cp1251 -*-
import random
from queue import Queue

class TreeNode:
    def __init__(self, value):
        self.v = value
        self.l = None  # ëåâûé óçåë
        self.r = None  # ïðàâûé óçåë

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
        Ïîèñê óçëà.
        Åñëè óçåë íå ïóñò, âûçûâàåì âñïîìîãàòåëüíóþ ôóíêöèþ ïîèñêà,
        èíà÷å âîçâðàùàåì None.
        '''
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        '''
        Âñïîìîãàòåëüíàÿ ðåêóðñèâíàÿ ôóíêöèÿ ïîèñêà.
        Åñëè óçåë íàéäåí, âîçâðàùàåì åãî. Åñëè çíà÷åíèå óçëà áîëüøå èñêîìîãî,
        ïðîäîëæàåì ïîèñê â ëåâîì ïîääåðåâå, åñëè îíî íå ïóñòîå. Åñëè çíà÷åíèå
        óçëà ìåíüøå èñêîìîãî, ïðîäîëæàåì ïîèñê â ïðàâîì ïîääåðåâå,
        åñëè îíî íå ïóñòîå.
        '''
        if val == node.v:
            return node.v
        elif (val < node.v and node.l != None):
            return self._find(val, node.l)
        elif (val > node.v and node.r != None):
            return self._find(val, node.r)

    def deleteTree(self):
        '''
        Óäàëåíèå äåðåâà.
        Óäàëÿåì êîðåíü, âñå îñòàëüíîå äåëàåò ñáîðùèê ìóñîðà.
        '''
        self.root = None
    def printTree(self):

        if self.root is not None:
            print("Äåðåâî:")
            self._printTree(self.root)
            print()
        else:
            print("Äåðåâî íå ñóùåñòâóåò")

    def _printTree(self, node):
        '''
        Âñïîìîãàòåëüíàÿ ðåêóðñèâíàÿ ôóíêöèÿ ïå÷àòè.
        '''
        if node is not None:
            print(str(node.v), end=' ')
            self._printTree(node.l)
            self._printTree(node.r)

    def BFS(self):
        '''
        Îáõîä äåðåâà â øèðèíó.
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
            print("Äåðåâî íå ñóùåñòâóåò")

    def countNodes(self):
        '''
        Ìåòîä äëÿ ïîäñ÷åòà êîëè÷åñòâà óçëîâ â áèíàðíîì äåðåâå ïîèñêà.
        Âûçûâàåì âñïîìîãàòåëüíóþ ôóíêöèþ äëÿ ðåêóðñèâíîãî ïîäñ÷åòà.
        '''
        return self._countNodes(self.root)

    def _countNodes(self, node):
        '''
        Âñïîìîãàòåëüíàÿ ðåêóðñèâíàÿ ôóíêöèÿ äëÿ ïîäñ÷åòà óçëîâ.
        Åñëè óçåë ïóñòîé, âîçâðàùàåì 0. Èíà÷å, ñ÷èòàåì êîðåíü + êîëè÷åñòâî óçëîâ
        â ëåâîì è ïðàâîì ïîääåðåâüÿõ.
        '''
        if node is None:
            return 0
        return 1 + self._countNodes(node.l) + self._countNodes(node.r)

    def countLeaves(self):
        '''
        Ìåòîä äëÿ ïîäñ÷åòà êîëè÷åñòâà ëèñòüåâ â áèíàðíîì äåðåâå ïîèñêà.
        Âûçûâàåì âñïîìîãàòåëüíóþ ôóíêöèþ äëÿ ðåêóðñèâíîãî ïîäñ÷åòà.
        '''
        return self._countLeaves(self.root)

    def _countLeaves(self, node):
        '''
        Âñïîìîãàòåëüíàÿ ðåêóðñèâíàÿ ôóíêöèÿ äëÿ ïîäñ÷åòà ëèñòüåâ.
        Åñëè óçåë ïóñòîé, âîçâðàùàåì 0. Åñëè óçåë ÿâëÿåòñÿ ëèñòîì, 
        âîçâðàùàåì 1. Â ïðîòèâíîì ñëó÷àå, ñ÷èòàåì ëèñòüÿ â ëåâîì è ïðàâîì ïîääåðåâüÿõ.
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

            # Äîáàâëÿåì ïðàâûé óçåë â ñòåê, ÷òîáû ñíà÷àëà îáðàáîòàòü ëåâûé
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

# Ïðèìåð èñïîëüçîâàíèÿ
min_val = 1
max_val = 100
n = 10

random_numbers = random.sample(range(min_val, max_val + 1), n)
print("Ñãåíåðèðîâàííûå ÷èñëà:", random_numbers)

tree = Tree()
tree.add(random_numbers[0])
for num in random_numbers[1:]:
    tree.add(num)

tree.printTree()
print("Êîëè÷åñòâî óçëîâ â äåðåâå:", tree.countNodes())
print("Êîëè÷åñòâî ëèñòüåâ â äåðåâå:", tree.countLeaves())
print("Âûñîòà äåðåâà:", tree.height())
print("Îáõîä â ãëóáèíó:", tree.depth_first_traversal())
print("Êðàñèâûé âûâîä áèíàðíîãî äåðåâà:")
tree.pretty_print()
