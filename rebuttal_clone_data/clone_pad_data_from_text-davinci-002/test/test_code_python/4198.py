def solution():
     initial_payment = 125
     payment_left = 75
     original_amount = initial_payment / (1 - (payment_left / 100))
     result = original_amount
     return result

print(solution())