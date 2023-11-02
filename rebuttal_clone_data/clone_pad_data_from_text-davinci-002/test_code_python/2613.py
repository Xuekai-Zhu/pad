def solution():
     cost_of_cheese = 7
     cost_of_beef = 5
     starting_money = 87
     money_after_beef = starting_money - cost_of_beef
     pounds_of_cheese = money_after_beef / cost_of_cheese
     result = pounds_of_cheese
     return result

print(solution())