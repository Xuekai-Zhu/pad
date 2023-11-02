def solution():
     ounces_per_bottle = 12
     petals_needed = 320 * ounces_per_bottle
     petals_per_rose = 8
     roses_per_bush = 12
     bushes_needed = petals_needed / (petals_per_rose * roses_per_bush)
     result = bushes_needed
     return result

print(solution())