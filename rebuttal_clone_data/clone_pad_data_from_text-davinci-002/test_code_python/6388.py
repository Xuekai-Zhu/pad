def solution():
     cans_of_soda = 24
     cans_of_soda_after_jeff = cans_of_soda - 6
     cans_of_soda_after_buying = cans_of_soda + (cans_of_soda_after_jeff / 2)
     cans_of_soda_before = cans_of_soda_after_buying - cans_of_soda
     result = cans_of_soda_before
     return result

print(solution())