def solution():
    total_cartons_needed = 42
    strawberries_owned = 2
    blueberries_owned = 7

    # Calculate the total number of cartons of berries Emilia already has
    total_owned = strawberries_owned + blueberries_owned

    # Calculate the number of cartons of berries Emilia needs to buy
    cartons_to_buy = total_cartons_needed - total_owned
    result = cartons_to_buy
    return result

print(solution())