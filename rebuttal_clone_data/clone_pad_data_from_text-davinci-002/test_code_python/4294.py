def solution():
    weeks_1_to_4 = 4
    savings_1_to_4 = 5
    weeks_5_to_8 = 4
    savings_5_to_8 = 10
    weeks_9_to_12 = 4
    savings_9_to_12 = 20
    total_savings = (weeks_1_to_4 * savings_1_to_4) + (weeks_5_to_8  * savings_5_to_8) + (weeks_9_to_12 * savings_9_to_12)
    result = total_savings
    return result

print(solution())