def solution():
    cost_per_game = 15
    total_cost = cost_per_game * 6
    money_paid = 100
    change_owed = money_paid - total_cost
    number_of_bills = change_owed / 5
    result = number_of_bills
    return result

print(solution())