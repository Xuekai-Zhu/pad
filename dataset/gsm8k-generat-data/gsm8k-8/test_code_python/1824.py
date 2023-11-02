def solution():
    # Define the number of chickens donated by Foster Farms
    foster_farms_chickens = 45

    # Calculate the number of water bottles donated by American Summits
    american_summits_water = 2 * foster_farms_chickens

    # Calculate the number of chickens donated by Hormel
    hormel_chickens = 3 * foster_farms_chickens

    # Calculate the number of chickens donated by Boudin Butchers
    boudin_chickens = hormel_chickens / 3

    # Calculate the number of water bottles donated by Del Monte Foods
    del_monte_water = american_summits_water - 30

    # Calculate the total number of food items donated
    total_items = foster_farms_chickens + american_summits_water + hormel_chickens + boudin_chickens + del_monte_water

    result = total_items
    return result

print(solution())