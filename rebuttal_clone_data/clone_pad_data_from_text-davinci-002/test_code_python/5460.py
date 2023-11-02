def solution():
    ounces_per_cup = 12
    ounces_drank_on_the_way = 3
    ounces_drank_at_work = 6
    ounces_left = ounces_per_cup - (ounces_drank_on_the_way + ounces_drank_at_work)
    result = ounces_left
    return result

print(solution())