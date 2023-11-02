def solution():
    # Define the prices of each drink
    cola_price = 3
    juice_price = 1.5
    water_price = 1

    # Calculate the total earnings from each type of drink
    cola_earnings = cola_price * 15
    juice_earnings = juice_price * 12
    water_earnings = water_price * 25

    # Calculate the total earnings for the day
    total_earnings = cola_earnings + juice_earnings + water_earnings
    result = total_earnings
    return result

print(solution())