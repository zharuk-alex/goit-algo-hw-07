from NodeClass import Node as BinaryTree

if __name__ == "__main__":
    # min value node
    root = BinaryTree(5)
    nodes = [3, 2, 4, 7, 6, 8]

    for n in nodes:
        root.insert(n)

    min_val_node = root.min_value_node()
    print("min value: ", min_val_node)  # 2
