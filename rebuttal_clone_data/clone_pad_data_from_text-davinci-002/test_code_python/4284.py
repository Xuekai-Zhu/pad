def solution():
     jeff_initial = 300
     jeff_donated = jeff_initial * .3
     jeff_remaining = jeff_initial - jeff_donated
     vicki_initial = jeff_initial * 2
     vicki_donated = vicki_initial * .75
     vicki_remaining = vicki_initial - vicki_donated
     total_remaining = jeff_remaining + vicki_remaining
     
     result = total_remaining
     return result

print(solution())