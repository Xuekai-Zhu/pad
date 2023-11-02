def solution():
    """In a certain country store, there are three kinds of bottled drinks. A cola, which costs $3, a juice for $1.5, and water for $1 per bottle. One day the store was able to sell 15 bottles of cola, 25 bottles of water, and 12 bottles of juice. How much did the shop earn?"""
    # Define the prices of each type of drink
    COLA_PRICE = 3
    JUICE_PRICE = 1.5
    WATER_PRICE = 1

    # Define the number of bottles sold of each type of drink
    cola_bottles = 15
    juice_bottles = 12
    water_bottles = 25

    # Calculate the total earnings for each type of drink
    cola_earnings = cola_bottles * COLA_PRICE
    juice_earnings = juice_bottles * JUICE_PRICE
    water_earnings = water_bottles * WATER_PRICE

    # Calculate the total earnings for all drinks
    total_earnings = cola_earnings + juice_earnings + water_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())