def solution():
    """Tim has 30 less apples than Martha, and Harry has half as many apples as Tim. If Martha has 68 apples, how many apples does Harry have?"""
    martha_apples = 68
    tim_apples = martha_apples - 30
    harry_apples = tim_apples / 2
    result = harry_apples
    return result

print(solution())