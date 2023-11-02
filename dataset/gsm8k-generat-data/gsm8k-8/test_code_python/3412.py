def solution():
    # Calculate how many glasses of chocolate milk he can make with the milk supply
    milk_glasses = 130 / 6.5

    # Calculate how many glasses of chocolate milk he can make with the chocolate syrup supply
    syrup_glasses = 60 / 1.5

    # Take the minimum of the two quantities to ensure he doesn't run out of either ingredient
    num_glasses = int(min(milk_glasses, syrup_glasses))

    # Calculate the total amount of chocolate milk he can make
    total_ounces = num_glasses * 8

    result = total_ounces
    return result

print(solution())