def solution():
     """Gina has two bank accounts. Each account has a quarter of the balance in Betty's account. If Betty's account balance is $3,456, what is the combined balance of both Gina's accounts?"""
     bettys_account = 3456
     ginas_account1 = bettys_account / 4
     ginas_account2 = ginas_account1
     total_balance = ginas_account1 + ginas_account2
     result = total_balance
     return result

print(solution())