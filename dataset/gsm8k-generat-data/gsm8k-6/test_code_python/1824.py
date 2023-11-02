def solution():
    # Calculate the number of food items donated by each company
    chickens = 45
    water = 2 * chickens
    hormel_chickens = 3 * chickens
    boudin_chickens = hormel_chickens // 3
    del_monte_water = water - 30

    # Calculate the total number of food items donated
    total_items = chickens + water + hormel_chickens + boudin_chickens + del_monte_water
    result = total_items
    return result

print(solution())