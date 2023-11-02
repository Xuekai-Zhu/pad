def solution():
    # Calculate the cost of each apple from the first store
    cost_per_apple1 = 3/6  # $3 for 6 apples

    # Calculate the cost of each apple from the second store
    cost_per_apple2 = 4/10  # $4 for 10 apples

    # Calculate the difference in cost per apple between the two stores
    savings_per_apple = (cost_per_apple1 - cost_per_apple2) * 100  # convert to cents

    result = savings_per_apple
    return result

print(solution())