def solution():
    days_in_April = 30
    days_walked = days_in_April - 4
    cost_per_day = 10
    total_cost = days_walked * cost_per_day
    books_cost = 50
    given_to_sister = 50
    money_left = total_cost - books_cost - given_to_sister
    result = money_left
    return result

print(solution())