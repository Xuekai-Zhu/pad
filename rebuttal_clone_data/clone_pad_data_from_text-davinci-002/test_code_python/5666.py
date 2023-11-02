def solution():
     total_cents = 70
     num_dimes = total_cents / 10
     num_nickels = num_dimes - 4
     result = num_nickels
     return result

print(solution())