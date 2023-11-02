def solution():
     initial_amount = 55
     shirt_amount = 7
     other_amount = shirt_amount * 3
     total_spent = shirt_amount + other_amount
     remaining_amount = initial_amount - total_spent
     result = remaining_amount
     return result

print(solution())