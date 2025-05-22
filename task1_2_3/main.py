class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# Функція отримання найбільшого значення відносно вузла
def get_max_in_node(node):
    if node.right:  # Якщо правий нащадок вузла існує, знайти його найбільше (саме праве) значення
        return get_max_in_node(node.right)
    return node.val  # Повернути значення найбільшого вузла

# Функція отримання найменшого значення відносно вузла
def get_min_in_node(node):
    if node.left:  # Якщо лівий нащадок вузла існує, знайти його найменше (саме ліве) значення
        return get_min_in_node(node.left)
    return node.val  # Повернути значення найменшого вузла

# Функція отримання суми значень вузла і всіх його нащадків
def sum_in_node(node):
    if not node:
        return 0
    return node.val + sum_in_node(node.left) + sum_in_node(node.right)

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)
root = delete(root, 7)
print(root)

# Знаходимо найбільше значення у двійковому дереві
print(f'Найбільше значення в нашому дереві - {get_max_in_node(root)}')

# Знаходимо найменше значення у двійковому дереві
print(f'Найменше значення в нашому дереві - {get_min_in_node(root)}')

# Додатково для вузлів пошук найбільших і найменших
search_3 = search(root, 3)
print(f'Найбільше значення у вузлі {search_3.val} нашого дерева - {get_max_in_node(search_3)}')
search_8 = search(root, 8)
print(f'Найменше значення у вузлі {search_8.val} нашого дерева - {get_min_in_node(search_8)}')

# Знаходження суми всіх значень в дереві і в конкретному вузлі
print(f'Сума значень в нашому дереві - {sum_in_node(root)}')
print(f'Сума значень у вузлі {search_3.val} нашого дерева - {sum_in_node(search_3)}')