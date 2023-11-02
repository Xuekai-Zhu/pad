def solution():
    apples_picked_day1 = 200/5
    apples_picked_day2 = apples_picked_day1*2
    apples_picked_day3 = apples_picked_day2 + 20
    total_apples_picked = apples_picked_day1 + apples_picked_day2 + apples_picked_day3
    remaining_apples = 200 - total_apples_picked
    result = remaining_apples
    return result

print(solution())