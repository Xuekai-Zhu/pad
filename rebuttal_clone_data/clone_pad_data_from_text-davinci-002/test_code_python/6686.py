def solution():
     guest_count = 120
     glasses_per_guest = 2
     servings_per_bottle = 6
     champagne_needed = guest_count * glasses_per_guest / servings_per_bottle
     result = champagne_needed
     return result

print(solution())