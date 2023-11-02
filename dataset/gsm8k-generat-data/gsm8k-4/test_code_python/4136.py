def solution():
    """Mary uses plastic grocery bags that can hold a maximum of twenty pounds. She buys 4 pounds of green beans, 6 pounds milk, and twice the amount of carrots as green beans. How many more pounds of groceries can Mary fit in that bag?"""
    # Define the maximum weight the bag can hold
    max_weight = 20

    # Calculate the weight of green beans, milk, and carrots
    green_beans = 4
    milk = 6
    carrots = 2 * green_beans
    
    # Calculate the total weight of groceries
    total_weight = green_beans + milk + carrots

    # Calculate the remaining weight that can fit in the bag
    remaining_weight = max_weight - total_weight
    
    # return the result
    result = remaining_weight
    return result

print(solution())