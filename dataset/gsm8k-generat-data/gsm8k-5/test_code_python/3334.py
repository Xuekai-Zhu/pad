def solution():
    total_animals = 360  # Total number of sheep and goats on the farm
    ratio_goats_sheep = 5 + 7  # Ratio of goats to sheep is 5:7
    goats = (5 / ratio_goats_sheep) * total_animals  # Number of goats on the farm
    sheep = (7 / ratio_goats_sheep) * total_animals  # Number of sheep on the farm

    # Calculate the number of goats sold and the revenue generated
    goats_sold = goats / 2
    goat_revenue = goats_sold * 40

    # Calculate the number of sheep sold and the revenue generated
    sheep_sold = sheep * (2 / 3)
    sheep_revenue = sheep_sold * 30

    # Calculate the total revenue generated from the sale of animals
    total_revenue = goat_revenue + sheep_revenue
    result = total_revenue
    return result

print(solution())