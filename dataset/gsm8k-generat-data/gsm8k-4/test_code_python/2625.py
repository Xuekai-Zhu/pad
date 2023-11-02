def solution():
    """55% of Toby's friends are boys and the rest are girls. If he has 33 friends who are boys, how many friends does he have who are girls?"""
    # Define the percentage of Toby's friends who are boys and the number of boys
    boys_percentage = 55
    boys = 33

    # Calculate the total number of friends
    total_friends = boys / (boys_percentage / 100)

    # Calculate the number of girls
    girls = total_friends - boys

    # return the result
    result = girls
    return result

print(solution())