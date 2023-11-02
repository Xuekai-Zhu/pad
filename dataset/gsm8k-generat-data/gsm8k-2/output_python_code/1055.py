def solution():
    """Maria is chopping up vegetables for a stew. She wants to cut up six times as many carrots as potatoes, twice as many onions as carrots, and 1/3 as many green beans as onions. If she has two potatoes, how many green beans does she need to cut?"""
    potatoes = 2
    carrots = 6 * potatoes
    onions = 2 * carrots
    green_beans = (1/3) * onions

    result = green_beans
    return result

print(solution())