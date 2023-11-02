def solution():
    apple_ratio = 1 / 2
    golden_delicious_apples = 20
    pink_lady_apples = 40
    apples_per_pint = golden_delicious_apples + pink_lady_apples
    apples_picked_per_hour = 240
    hours_worked = 5
    total_apples_picked = apples_picked_per_hour * hours_worked
    total_pints = total_apples_picked / apples_per_pint
    result = total_pints
    return result

print(solution())