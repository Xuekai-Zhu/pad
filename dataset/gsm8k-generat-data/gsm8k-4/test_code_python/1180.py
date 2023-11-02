def solution():
    """A local restaurant is offering an 8 piece fried chicken bucket and 2 sides for $12.00 that will feed 6 people. If Monty was having a family reunion for 36 family members, how much will it cost him to buy enough chicken and sides to feed everyone one serving?"""
    # Define the cost of the chicken bucket and sides combo for 6 people
    COMBO_COST = 12

    # Define the number of people each combo can feed
    COMBO_SERVINGS = 6

    # Define the number of pieces of chicken in each combo
    CHICKEN_PIECES_PER_COMBO = 8

    # Define the number of sides in each combo
    SIDES_PER_COMBO = 2

    # Calculate the total number of servings needed
    total_servings = 36

    # Calculate the number of combos needed
    total_combos = total_servings // COMBO_SERVINGS
    if total_servings % COMBO_SERVINGS != 0:
        total_combos += 1

    # Calculate the total cost of the chicken and sides
    total_cost = total_combos * COMBO_COST

    result = total_cost
    return result

print(solution())