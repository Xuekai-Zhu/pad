def solution():
    households_visited_per_day = 20
    days_worked = 5
    households_giving_money = households_visited_per_day / 2
    amount_given_per_household = 40
    total_collected = households_giving_money * amount_given_per_household * days_worked
    result = total_collected
    return result

print(solution())