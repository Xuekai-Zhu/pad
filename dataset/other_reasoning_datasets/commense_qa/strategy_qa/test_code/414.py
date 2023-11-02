def solution():
    office_length = 35
    office_width = 29
    kia_length = 14.3
    kia_width = 5.6
    if kia_length <= office_length and kia_width <= office_width:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())