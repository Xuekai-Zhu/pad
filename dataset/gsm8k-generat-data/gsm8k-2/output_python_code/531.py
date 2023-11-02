def solution():
    """The batting cage sells golf balls by the dozen. They charge $30 for 3 dozen. Dan buys 5 dozen, Gus buys 2 dozen, and Chris buys 48 golf balls. How many golf balls do they purchase in total, assuming 12 golf balls are 1 dozen?"""
    price_per_dozen = 30/3
    dan_dozen = 5
    gus_dozen = 2
    chris_dozen = 4
    chris_balls = 48
    total_dozen = dan_dozen + gus_dozen + chris_dozen
    total_balls = total_dozen * 12 + chris_balls
    result = total_balls
    return result

print(solution())