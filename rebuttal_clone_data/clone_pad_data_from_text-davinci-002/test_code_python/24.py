def solution():
     """Mary does her grocery shopping on Saturday. She does her shopping only at a specific store where she is allowed a credit of $100, which must be paid in full before her next shopping trip. That week she spent the full credit limit and paid $15 of it on Tuesday and $23 of it on Thursday. How much credit will Mary need to pay before her next shopping trip?"""
     credit_limit = 100
     credit_used = 15 + 23
     credit_left = credit_limit - credit_used
     result = credit_left
     
     return result

print(solution())