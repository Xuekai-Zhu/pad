def solution():
    # Calculate the total number of oranges harvested by the three sisters
    total_oranges = 110 * (600 + 400 + 500)  # Gabriela's grove produced 600 oranges per tree, Alba harvested 400 per tree, Maricela's trees produced 500 oranges
    total_cups = total_oranges/3  # 3 medium-sized oranges can make 1 cup of juice

    # Calculate the total revenue from selling the orange juice
    total_revenue = total_cups * 4  # Each cup of juice is sold for $4

    result = total_revenue
    return result

print(solution())