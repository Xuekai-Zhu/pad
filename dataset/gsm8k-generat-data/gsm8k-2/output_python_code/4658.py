def solution():
    """There are 48 passengers on the bus. Two-thirds of the passengers are women and the rest are men. If one-eighth of the men are standing, how many men are seated?"""
    total_passengers = 48
    women_passengers = total_passengers * 2/3
    men_passengers = total_passengers - women_passengers
    standing_men = men_passengers * 1/8
    seated_men = men_passengers - standing_men
    result = seated_men
    return result

print(solution())