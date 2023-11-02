def solution():
     money_left = 104
     trips_per_month = 4
     money_spent_per_trip = 2
     total_money_spent = trips_per_month * money_spent_per_trip
     initial_money = money_left + total_money_spent
     result = initial_money
     
     return result

print(solution())