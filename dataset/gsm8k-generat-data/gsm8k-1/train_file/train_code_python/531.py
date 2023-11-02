def solution():
    """The batting cage sells golf balls by the dozen. They charge $30 for 3 dozen. Dan buys 5 dozen, Gus buys 2 dozen, and Chris buys 48 golf balls. How many golf balls do they purchase in total, assuming 12 golf balls are 1 dozen?"""
    price_for_three_dozen = 30
    golf_balls_per_dozen = 12
    
    total_golf_balls = 5 * golf_balls_per_dozen + 2 * golf_balls_per_dozen + 48
    result = total_golf_balls
    
    return result

print(solution())