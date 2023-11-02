def solution():
    """Krista started raising chickens. She has 10 hens who lay eggs. She sells the eggs for $3 a dozen. In four weeks, she sold $120 worth of eggs. If she sold all the eggs her hens laid, how many eggs does each hen lay a week?"""
    # Define the number of hens and the selling price of eggs
    hens = 10
    egg_price = 3

    # Calculate the total amount of eggs sold in four weeks
    total_eggs_sold = 120 / egg_price * 12

    # Calculate the average number of eggs laid per week per hen
    eggs_per_week_per_hen = total_eggs_sold / (hens * 4)

    # Round the answer to the nearest integer
    result = round(eggs_per_week_per_hen)
    return result

print(solution())