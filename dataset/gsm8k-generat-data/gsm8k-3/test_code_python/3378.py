def solution():
    """Krista started raising chickens. She has 10 hens who lay eggs. She sells the eggs for $3 a dozen. In four weeks, she sold $120 worth of eggs. If she sold all the eggs her hens laid, how many eggs does each hen lay a week?"""
    # Define the price per dozen and the total sales
    PRICE_PER_DOZEN = 3
    TOTAL_SALES = 120

    # Calculate the total dozens of eggs sold
    dozens_sold = TOTAL_SALES / PRICE_PER_DOZEN

    # Calculate the total eggs sold
    eggs_sold = dozens_sold * 12

    # Calculate the average number of eggs laid per hen per week
    eggs_per_week = eggs_sold / (10 * 4)

    # Display the result
    result = eggs_per_week
    return result

print(solution())