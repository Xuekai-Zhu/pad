def solution():
    """Greg bought a 20-pack of granola bars to eat at lunch for the week. He set aside one for each day of the week, traded three of the remaining bars to his friend Pete for a soda, and gave the rest to his two sisters. How many did each sister get when they split them evenly?"""
    # Define the total number of granola bars
    total_bars = 20

    # Define the number of bars Greg kept for himself
    gregs_bars = 7

    # Define the number of bars Greg traded to Pete
    petes_bars = 3

    # Calculate the number of bars Greg gave to his two sisters
    sisters_bars = total_bars - gregs_bars - petes_bars

    # Calculate the number of bars each sister received
    bars_per_sister = sisters_bars / 2

    # Display the number of bars each sister received
    result = bars_per_sister
    return result

print(solution())