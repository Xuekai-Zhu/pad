def solution():
    """Maria is chopping up vegetables for a stew. She wants to cut up six times as many carrots as potatoes, twice as many onions as carrots, and 1/3 as many green beans as onions. If she has two potatoes, how many green beans does she need to cut?"""
    # Define the number of potatoes
    potatoes = 2

    # Calculate the number of carrots
    carrots = 6 * potatoes

    # Calculate the number of onions
    onions = 2 * carrots

    # Calculate the number of green beans
    green_beans = 1/3 * onions

    # Display the number of green beans
    result = green_beans
    return result

print(solution())