def solution():
    unemployed_in_1933 = 15000000
    tiger_stadium_capacity = 50000
    if unemployed_in_1933 <= tiger_stadium_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())