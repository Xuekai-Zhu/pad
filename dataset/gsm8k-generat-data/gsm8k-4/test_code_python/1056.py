def solution():
    """Maria is chopping up vegetables for a stew. She wants to cut up six times as many carrots as potatoes, twice as many onions as carrots, and 1/3 as many green beans as onions. If she has two potatoes, how many green beans does she need to cut?"""
    # Define the number of potatoes
    potatoes = 2

    # Calculate the number of carrots
    carrots = potatoes * 6

    # Calculate the number of onions
    onions = carrots * 2

    # Calculate the number of green beans
    green_beans = onions * (1/3)

    # return the result
    result = green_beans
    return result

print(solution())