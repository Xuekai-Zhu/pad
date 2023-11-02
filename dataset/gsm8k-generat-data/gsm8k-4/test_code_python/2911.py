def solution():
    """Greg bought a 20-pack of granola bars to eat at lunch for the week. He set aside one for each day of the week, traded three of the remaining bars to his friend Pete for a soda, and gave the rest to his two sisters. How many did each sister get when they split them evenly?"""
    # Define the number of granola bars Greg bought
    granola_bars = 20

    # Set aside one granola bar for each day of the week
    granola_bars -= 7

    # Trade three granola bars for a soda
    granola_bars -= 3

    # Divide the remaining granola bars equally among two sisters
    granola_bars_per_sister = granola_bars / 2

    # Return the result
    result = granola_bars_per_sister
    return result

print(solution())