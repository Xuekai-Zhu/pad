def solution():
     total_pens = 62 + 43
     total_taken = 37 + 41
     remaining_pens = total_pens - total_taken
     pens_each = remaining_pens / 3
     result = pens_each
 
    return result

print(solution())