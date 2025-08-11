class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_from_level_order(values):
    if not values or values[0] in ("null", -1):
        return None

    root = Node(int(values[0]))
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        
        # Left child
        if i < len(values) and values[i] not in ("null", -1):
            current.left = Node(int(values[i]))
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] not in ("null", -1):
            current.right = Node(int(values[i]))
            queue.append(current.right)
        i += 1

    return root

def zigzag_traversal(root):
    if not root:
        return []
    current_level = [root]
    next_level = []
    result = []
    left_to_right = True

    while current_level:
        level_vals = []
        while current_level:
            node = current_level.pop()
            level_vals.append(node.val)
            if left_to_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
        result.append(level_vals)
        current_level, next_level = next_level, []
        left_to_right = not left_to_right
    return result

def solve_zigzag():
    raw_values = input("Enter tree nodes in level order (use 'null' or -1 for no node): ").strip().split()
    # Convert numeric strings to int except "null"
    processed_values = []
    for v in raw_values:
        if v.lower() == "null":
            processed_values.append("null")
        else:
            try:
                processed_values.append(int(v))
            except:
                processed_values.append("null")
    root = build_tree_from_level_order(processed_values)
    print("Zigzag traversal:", zigzag_traversal(root))

if __name__ == "__main__":
    solve_zigzag()
