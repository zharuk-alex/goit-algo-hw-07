from NodeClass import Node as BinaryTree

if __name__ == "__main__":
    # sum of values
    root = BinaryTree(5)
    nodes = [3, 2, 4, 7, 6, 8]

    for n in nodes:
        root.insert(n)

    sum_values = root.sum_values()
    print("sum of values: ", sum_values)  # 35
