def solution():
     total_chargers = 24
     laptop_chargers = 5
     phone_chargers = total_chargers / (laptop_chargers + 1)
     result = phone_chargers
     return result

print(solution())