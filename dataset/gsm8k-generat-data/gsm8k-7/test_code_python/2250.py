def solution():
    one_serving_chickpeas = 1  # in cups
    can_chickpeas = 16  # in ounces
    one_cup_chickpeas = 6  # in ounces
    num_servings = 20

    # Calculate the total number of cups of chickpeas needed for 20 servings
    total_chickpeas = one_serving_chickpeas * num_servings

    # Calculate the total number of ounces of chickpeas needed
    total_chickpeas_ounces = total_chickpeas * one_cup_chickpeas

    # Calculate the total number of cans of chickpeas required, rounding up to the nearest integer
    num_cans = int((total_chickpeas_ounces / can_chickpeas) + 0.5)

    result = num_cans
    return result

print(solution())