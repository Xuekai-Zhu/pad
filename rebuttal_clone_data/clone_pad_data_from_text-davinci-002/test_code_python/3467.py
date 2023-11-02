def solution():
     num_bills = 15
     bills_spent = 20
     percent_spent = bills_spent / 100
     num_bills_left = num_bills - (num_bills * percent_spent)
     exchange_rate = 1.5
     money_received = num_bills_left * exchange_rate
     result = money_received
     return result

print(solution())