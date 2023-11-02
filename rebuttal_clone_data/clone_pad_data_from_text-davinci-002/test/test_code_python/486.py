def solution():
     hamburger_per_meatball = 1/8
     total_hamburger = 4
     meatballs_made = total_hamburger / hamburger_per_meatball
     family_size = 8
     meatballs_per_person = meatballs_made / family_size
     result = meatballs_per_person
     return result

print(solution())