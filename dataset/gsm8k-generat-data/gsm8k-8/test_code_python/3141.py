def solution():
    breakfast_cal = 500
    lunch_cal = 1.25 * breakfast_cal
    dinner_cal = 2 * lunch_cal
    shake_cal = 300
    total_cal = 3 * (breakfast_cal + lunch_cal + dinner_cal) + 3 * shake_cal
    result = total_cal
    return result

print(solution())