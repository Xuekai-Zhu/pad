def solution():
    largest_baby_weight = 22
    average_skull_weight = 10.5
    if average_skull_weight < largest_baby_weight:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())