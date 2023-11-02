def solution():
     borrowed_amount = 100
     interest_rate = 10
     interest_amount = borrowed_amount * (interest_rate / 100)
     total_amount_owed = borrowed_amount + interest_amount
     result = total_amount_owed
     return result

print(solution())