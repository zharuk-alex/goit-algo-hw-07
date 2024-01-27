from NodeClass import Node as BinaryTree

if __name__ == "__main__":
    # max value node
    root = BinaryTree(5)
    nodes = [3, 2, 4, 7, 6, 8]

    for n in nodes:
        root.insert(n)

    max_val_node = root.max_value_node()
    print("max value: ", max_val_node.val)  # 8
