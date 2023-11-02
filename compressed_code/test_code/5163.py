def solution():
    
    guests = 120
    glasses_per_guest = 2
    total_glasses = guests * glasses_per_guest
    servings_per_bottle = 6
    bottles_needed = total_glasses / servings_per_bottle
    result = bottles_needed
    return result

print(solution())