def solution():
    servings_per_cup = 1
    cups_per_night = 2
    ounces_per_container = 16
    servings_per_ounce = 6

    total_servings = servings_per_cup * cups_per_night * nights
    total_ounces = total_servings / servings_per_ounce
    nights = int(ounces_per_container / total_ounces)

    result = nights
    return result

print(solution())