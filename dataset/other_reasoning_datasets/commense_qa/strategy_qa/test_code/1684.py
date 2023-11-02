def solution():
    founding_year = 1946
    is_composite = False
    for i in range(2, founding_year):
        if founding_year % i == 0:
            is_composite = True
            break
    if is_composite:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())