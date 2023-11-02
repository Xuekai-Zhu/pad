def solution():
    # Define the ratio of goats to sheep
    goat_sheep_ratio = 5/7
    # Calculate the number of goats on the farm
    total_animals = 360
    total_goats = goat_sheep_ratio * total_animals
    # Calculate the number of goats sold and the income from their sale
    goats_sold = 0.5 * total_goats
    goat_income = goats_sold * 40
    # Calculate the number of sheep sold and the income from their sale
    sheep_sold = (2/3) * (total_animals - total_goats)
    sheep_income = sheep_sold * 30
    # Calculate the total income from the sale of animals
    total_income = goat_income + sheep_income
    result = total_income
    return result

print(solution())