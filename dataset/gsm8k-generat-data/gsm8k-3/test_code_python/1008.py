def solution():
    """Lana aims to sell 20 muffins at the bake sale. She sells 12 muffins in the morning. She sells another 4 in the afternoon. How many more muffins does Lana need to sell to hit her goal?"""
    # Define the total number of muffins Lana aims to sell
    GOAL = 20

    # Define the number of muffins Lana has sold so far
    sold_so_far = 12 + 4

    # Calculate the number of muffins Lana still needs to sell
    remaining = GOAL - sold_so_far

    # Display the number of muffins Lana still needs to sell
    result = remaining
    return result

print(solution())