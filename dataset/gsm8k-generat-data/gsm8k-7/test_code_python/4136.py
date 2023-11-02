def solution():
    max_weight = 20
    green_beans = 4
    milk = 6
    carrots = 2 * green_beans
    
    # Calculate the total weight of groceries
    total_weight = green_beans + milk + carrots
    
    # Calculate the remaining weight that can fit in the bag
    remaining_weight = max_weight - total_weight
    result = remaining_weight
    return result

print(solution())