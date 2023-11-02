def solution():
    """Five food companies sponsored a local food bank. Foster Farms donated 45 dressed chickens; American Summits donated twice the number of bottled water than the number of dressed chicken donated by Foster Farms; Hormel donated three times the number of dressed chickens that Foster Farms donated; Boudin Butchers donated one-third of the number of dressed chickens that Hormel donated; Del Monte Foods donated 30 fewer bottles of water than American Summits. How many food items did the companies donate in total?"""
    # Define the number of dressed chickens donated by Foster Farms
    chickens = 45

    # Define the number of bottled water donated by American Summits
    water = 2 * chickens

    # Define the number of dressed chickens donated by Hormel
    hormel_chickens = 3 * chickens

    # Define the number of dressed chickens donated by Boudin Butchers
    boudin_chickens = hormel_chickens // 3

    # Define the number of bottled water donated by Del Monte Foods
    del_monte_water = water - 30

    # Calculate the total number of food items donated
    total_items = chickens + water + hormel_chickens + boudin_chickens + del_monte_water

    # Display the total number of food items
    result = total_items
    return result

print(solution())