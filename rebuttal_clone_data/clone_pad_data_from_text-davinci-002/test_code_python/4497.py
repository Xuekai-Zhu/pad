def solution():
     cans_needed = 600
     people_fed = 40
     percent_ decrease = 30
     new_people_fed = people_fed - (people_fed * (percent_decrease / 100))
     new_cans_needed = cans_needed - (cans_needed * (percent_decrease / 100))
     result = new_cans_needed
     return result

print(solution())