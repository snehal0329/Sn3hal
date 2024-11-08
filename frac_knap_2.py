def fractional_knapsack(weights, values, capacity):
    res = 0 

    # Pair (weight, value) and sort based on value/weight ratio in descending order
    items = list(zip(weights, values))
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    for weight, value in items:
        if capacity <= 0:  # If the bag is full, stop
            break
        
        if weight <= capacity:  # If the whole item can fit
            res += value
            capacity -= weight
        else:  # Take a fraction of the item
            res += value * (capacity / weight)
            capacity = 0  # Bag is full, no remaining capacity

    # Return the maximum value that can be carried in the knapsack
    return res

if __name__ == "__main__":
    # Taking user input for weights, values, and capacity
    n = int(input("Enter the number of items: "))  # Number of items
    weights = []
    values = []

    # Getting weights and values from the user
    for i in range(n):
        weight = float(input(f"Enter the weight of item {i + 1}: "))
        value = float(input(f"Enter the value of item {i + 1}: "))
        weights.append(weight)
        values.append(value)

    # Taking capacity of the knapsack
    capacity = float(input("Enter the capacity of the knapsack: "))
    # Calculate and display the maximum value that can be carried in the knapsack
    result = fractional_knapsack(weights, values, capacity)
    print(f"Maximum value in Knapsack = {result:.2f}")
