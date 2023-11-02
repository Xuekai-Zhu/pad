def solution():
    """Amber buys 7 guppies for her pond. Several days later, she sees 3 dozen baby guppies swimming around. Two days after that, she sees 9 more baby guppies. How many guppies does she have now?"""
    initial_guppies = 7
    baby_guppies = 3 * 12 + 9
    total_guppies = initial_guppies + baby_guppies
    result = total_guppies
    return result

print(solution())