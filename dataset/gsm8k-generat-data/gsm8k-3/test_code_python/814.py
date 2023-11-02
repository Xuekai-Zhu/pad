def solution():
    """Every Sunday, Sean picks up 1 almond croissant and 1 salami and cheese croissant that are $4.50 each.  He also grabs a plain croissant for $3.00 and a loaf of focaccia for $4.00.  On his way home he stops and picks up 2 lattes for $2.50 each.  How much did he spend?"""
    # Define the prices
    ALMOND_CROISSANT_PRICE = 4.5
    SALAMI_CROISSANT_PRICE = 4.5
    PLAIN_CROISSANT_PRICE = 3.0
    FOCACCIA_PRICE = 4.0
    LATTE_PRICE = 2.5

    # Calculate the total cost of croissants
    croissant_cost = ALMOND_CROISSANT_PRICE + SALAMI_CROISSANT_PRICE + PLAIN_CROISSANT_PRICE

    # Calculate the total cost of Sean's purchases
    total_cost = croissant_cost + FOCACCIA_PRICE + (2 * LATTE_PRICE)

    # Display the total cost
    result = total_cost
    return result

print(solution())