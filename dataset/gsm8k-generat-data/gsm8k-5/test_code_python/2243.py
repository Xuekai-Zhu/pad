def solution():
    lilacs_sold = 10  # Ginger sold 10 lilacs on Tuesday
    roses_sold = 3 * lilacs_sold  # Ginger sold 3 times more roses than lilacs
    gardenias_sold = lilacs_sold / 2  # Ginger sold half as many gardenias as lilacs

    # Calculate the total number of flowers sold on Tuesday
    total_flowers_sold = lilacs_sold + roses_sold + gardenias_sold
    result = total_flowers_sold
    return result

print(solution())