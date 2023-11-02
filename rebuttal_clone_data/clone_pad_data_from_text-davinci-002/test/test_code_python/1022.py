def solution():
     initial_doves = 20
     eggs_laid = 3 * initial_doves
     eggs_hatched = (3/4) * eggs_laid
     total_doves = initial_doves + eggs_hatched
     result = total_doves
     return result

print(solution())