def solution():
    """Jason is mixing a batch of black paint. He needs to add 2 grams of charcoal for every 30 ml of water. If he adds 900 ml of water, how much charcoal does he add?"""
    # Define the amount of charcoal needed per ml of water
    CHARCOAL_PER_WATER = 2 / 30

    # Define the amount of water Jason added
    water_added = 900

    # Calculate the amount of charcoal needed
    charcoal_needed = CHARCOAL_PER_WATER * water_added

    # Display the amount of charcoal needed
    result = charcoal_needed
    return result

print(solution())