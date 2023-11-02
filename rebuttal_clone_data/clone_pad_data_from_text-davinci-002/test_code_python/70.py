def solution():
    """Tim has 30 less apples than Martha, and Harry has half as many apples as Tim. If Martha has 68 apples, how many apples does Harry have?"""
    apples_martha = 68
    apples_tim = apples_martha - 30
    apples_harry = apples_tim / 2
    result = apples_harry
    return result

print(solution())