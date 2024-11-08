def solve_knapsack():
    # Number of items input
    n = int(input("Enter the number of items: "))
    
    weights = []
    values = []

    # Getting weights and values from the user
    for i in range(n):
        weight = int(input(f"Enter the weight of item {i + 1}: "))  # Using int for weight
        value = int(input(f"Enter the value of item {i + 1}: "))   # Using int for value
        weights.append(weight)
        values.append(value)

    # Taking capacity of the knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))  # Using int for capacity

    # DP table where dp[i][w] will store the maximum value that can be obtained 
    # with the first i items and a knapsack capacity of w.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table using the bottom-up approach
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # If the weight of the current item is less than or equal to the capacity
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]  # If the current item's weight exceeds the capacity, skip it

    # The bottom-right cell of the table contains the maximum value that can be obtained
    print(f"The maximum value that can be obtained: {dp[n][capacity]}")

if __name__ == "__main__":
    solve_knapsack()
