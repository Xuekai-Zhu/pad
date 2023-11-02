def solution():
    saturday = 80
    monday = saturday - 20
    wednesday = monday + 50
    friday = (saturday + monday)

    total = saturday + monday + wednesday + friday
    expected_total = 350
    difference = total - expected_total
    result = difference
    return result

print(solution())