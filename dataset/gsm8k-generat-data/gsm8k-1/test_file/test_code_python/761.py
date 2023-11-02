def solution():
    """George has 45% more pears than bananas. If George has 200 bananas, how many fruits does George have?"""
    percent_more = 45
    bananas = 200
    pears = bananas * (1 + (percent_more / 100))
    total_fruits = bananas + pears
    result = total_fruits
    return result

print(solution())