def solution():
    doug_age = 40  # age of Doug
    sum_age = 90  # sum of their ages
    betty_age = sum_age - doug_age  # age of Betty

    cost = betty_age * 2  # cost of one pack of nuts
    total_cost = cost * 20  # cost of 20 packs of nuts

    result = total_cost
    return result

print(solution())