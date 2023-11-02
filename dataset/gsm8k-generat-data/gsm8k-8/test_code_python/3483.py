def solution():
    households_visited = 20 * 5
    households_gave_money = households_visited / 2
    money_per_household = 2 * 20  # a pair of 20s
    total_money_collected = households_gave_money * money_per_household
    result = total_money_collected
    return result

print(solution())