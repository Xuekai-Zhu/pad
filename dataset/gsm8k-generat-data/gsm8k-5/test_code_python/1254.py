def solution():
    total_cartons = 42  # Emilia needs 42 cartons of berries
    strawberries = 2  # Emilia already has 2 cartons of strawberries
    blueberries = 7  # Emilia already has 7 cartons of blueberries

    # Calculate the number of cartons Emilia needs to buy
    cartons_to_buy = total_cartons - (strawberries + blueberries)
    result = cartons_to_buy
    return result

print(solution())