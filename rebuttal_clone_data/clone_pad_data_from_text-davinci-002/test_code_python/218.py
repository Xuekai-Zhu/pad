def solution():
     """Ravi has some coins. He has 2 more quarters than nickels and 4 more dimes than quarters. If he has 6 nickels, how much money does he have?"""
     quarters = 6 + 2
     dimes = quarters + 4
     nickels = quarters - 2
     total = quarters + dimes + nickels
     result = total
     return result

print(solution())