def solution():
    """Derrick measures the length of his yard. The length of Alex's yard is half the size of Derrick's and the length of Brianne's yard is 6 times the size of Alex's. If Brianne's yard is 30 yards long, how long is Derrick's yard, in yards?"""
    brianne_yard = 30
    alex_yard = brianne_yard / 6
    derrick_yard = alex_yard * 2
    result = derrick_yard
    return result

print(solution())