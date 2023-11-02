def solution():
     """The profit from a business transaction is shared among 2 business partners, Mike and Johnson in the ratio 2:5 respectively. If Johnson got $2500, how much will Mike have after spending some of his share on a shirt that costs $200?"""
     profit = 2500
     mike_ratio = 2
     johnson_ratio = 5
     mike_share = profit * (mike_ratio / (mike_ratio + johnson_ratio))
     mike_spending = 200
     mike_total = mike_share - mike_spending
     result = mike_total
     return result

print(solution())