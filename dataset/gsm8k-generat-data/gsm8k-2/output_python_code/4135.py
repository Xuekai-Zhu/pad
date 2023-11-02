def solution():
    """Mary uses plastic grocery bags that can hold a maximum of twenty pounds. She buys 4 pounds of green beans, 6 pounds milk, and twice the amount of carrots as green beans. How many more pounds of groceries can Mary fit in that bag?"""
    bag_capacity = 20
    green_beans = 4
    milk = 6
    carrots = 2 * green_beans
    total_weight = green_beans + milk + carrots
    remaining_capacity = bag_capacity - total_weight
    result = remaining_capacity
    return result

print(solution())