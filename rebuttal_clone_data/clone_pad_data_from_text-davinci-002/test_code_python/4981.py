def solution():
     akeno_amount = 2985
     lev_amount = akeno_amount / 3
     ambrocio_amount = lev_amount - 177
     total_amount = akeno_amount + lev_amount + ambrocio_amount
     result = total_amount - (lev_amount + ambrocio_amount)
     return result

print(solution())