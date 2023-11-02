def solution():
    # Calculate the total amount of soy sauce needed in cups
    total_soy_sauce_cups = 2 + 1 + 3  

    # Convert cups to ounces and calculate total amount of soy sauce needed in ounces
    total_soy_sauce_ounces = total_soy_sauce_cups * 8  

    # Calculate the number of bottles needed, rounding up to the nearest whole bottle
    bottles_needed = (total_soy_sauce_ounces / 16) 
    bottles_needed = math.ceil(bottles_needed)

    result = bottles_needed
    return result

print(solution())