def solution():
    total_earned = 100
    pay_per_pound = 2
    berries_picked_on_monday = 8
    berries_picked_on_tuesday = berries_picked_on_monday * 3
    berries_picked_on_wednesday = 0
    berries_picked_on_thursday = total_earned / pay_per_pound - (berries_picked_on_monday + berries_picked_on_tuesday)
    result = berries_picked_on_thursday
    return result

print(solution())