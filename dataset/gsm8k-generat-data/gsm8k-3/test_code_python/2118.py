def solution():
    """Brandon has been fired from half the businesses in town and has quit from a third of them. If there are 72 business in town, how many businesses can he still apply to?"""
    # Calculate the number of businesses Brandon has left
    businesses_left = 72 - (72 // 2) - (72 // 3)

    # Display the number of businesses Brandon can still apply to
    result = businesses_left
    return result

print(solution())