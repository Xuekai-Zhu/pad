def solution():
    katy_flour = 3 * 5 * 16  # Katy brought three 5-pound bags of flour, converted to ounces
    wendi_flour = 2 * katy_flour  # Wendi brought twice as much flour as Katy
    carrie_flour = wendi_flour - 5 * 16  # Carrie brought 5 pounds less than the amount of flour Wendi brought, converted to ounces

    # Calculate how much more flour Carrie brought than Katy, in ounces
    difference = carrie_flour - katy_flour
    result = difference
    return result

print(solution())