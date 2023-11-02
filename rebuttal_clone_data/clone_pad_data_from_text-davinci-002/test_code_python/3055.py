def solution():
     vinegar = 100
     percent_evaporated = 20
     year_1 = vinegar - (vinegar * (percent_evaporated/100))
     year_2 = year_1 - (year_1 * (percent_evaporated/100))
     percent_left = year_2
     result = percent_left
     return result

print(solution())