def solution():
    households_visited = 20 * 5  # Mark visits 20 households a day for 5 days
    households_giving = households_visited / 2  # Half of the households give money
    money_per_household = 2 * 20  # Each household gives a pair of 20s, which is $40
    total_money_collected = households_giving * money_per_household
    result = total_money_collected
    return result

print(solution())