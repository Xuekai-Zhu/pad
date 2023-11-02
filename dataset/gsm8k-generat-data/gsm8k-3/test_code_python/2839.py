def solution():
    """Jacob is making s'mores. Each s'more takes two graham crackers and one marshmallow. If Jacob has 48 graham crackers and 6 marshmallows, how many more marshmallows does he need to buy?"""
    # Calculate the maximum number of s'mores Jacob can make with the available ingredients
    max_smores = min(48 // 2, 6)

    # Calculate the number of marshmallows Jacob needs to buy to make more s'mores
    marshmallows_needed = (max_smores * 2) - 6

    # Display the number of marshmallows needed to buy
    result = marshmallows_needed
    return result

print(solution())