def solution():
    """There are 48 passengers on the bus. Two-thirds of the passengers are women and the rest are men. If one-eighth of the men are standing, how many men are seated?"""
    total_passengers = 48
    women_ratio = 2/3
    men_ratio = 1 - women_ratio
    men_total = total_passengers * men_ratio
    standing_ratio = 1/8
    men_standing = men_total * standing_ratio
    men_seated = men_total - men_standing
    result = men_seated
    return result

print(solution())