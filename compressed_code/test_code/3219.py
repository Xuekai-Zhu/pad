def solution():
    
    bag_capacity = 20
    green_beans = 4
    milk = 6
    carrots = 2 * green_beans
    total_weight = green_beans + milk + carrots
    remaining_capacity = bag_capacity - total_weight
    result = remaining_capacity
    return result

print(solution())