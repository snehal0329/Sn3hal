import heapq

# Creating Huffman tree node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # frequency of symbol
        self.symbol = symbol  # symbol name (character)
        self.left = left  # left node of current node
        self.right = right  # right node of current node
        self.huff = ''  # tree direction (0/1)

    # For heapq to compare nodes based on frequency
    def __lt__(self, nxt):
        return self.freq < nxt.freq

# Function to print the Huffman codes
def print_nodes(node, val=''):
    newval = val + node.huff
    # if node is not an edge node then traverse inside it
    if node.left:
        print_nodes(node.left, newval)
    if node.right:
        print_nodes(node.right, newval)

    # if node is an edge node, display its huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newval}")

if __name__ == "__main__":
    chars = input("Enter characters (comma separated): ").split(',')
    freq = list(map(int, input("Enter corresponding frequencies (comma separated): ").split(',')))
    
    # Create the initial list of nodes
    nodes = []

    # Convert characters and frequencies into Huffman tree nodes
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freq[i], chars[i]))

    # Build the Huffman tree using the greedy approach
    while len(nodes) > 1:
        left = heapq.heappop(nodes)  # Node with the smallest frequency
        right = heapq.heappop(nodes)  # Node with the second smallest frequency

        left.huff = '0'  # Assign '0' to the left child
        right.huff = '1'  # Assign '1' to the right child

        # Create a new node combining the two smallest nodes
        new_node = Node(left.freq + right.freq, '', left, right)

        # Push the new node back into the priority queue
        heapq.heappush(nodes, new_node)

    # Print the Huffman codes starting from the root of the tree
    print("Huffman Encoding:")
    print_nodes(nodes[0])  # Passing the root of the Huffman Tree
