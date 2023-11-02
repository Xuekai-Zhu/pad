def solution():
    # Define the weights of the groceries
    green_beans_weight = 4
    milk_weight = 6
    carrots_weight = 2 * green_beans_weight

    # Calculate the total weight of the groceries
    total_weight = green_beans_weight + milk_weight + carrots_weight

    # Calculate how many more pounds can fit in the bag
    remaining_weight = 20 - total_weight
    result = remaining_weight
    return result

print(solution())