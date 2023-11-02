def solution():
    """Jason is mixing a batch of black paint. He needs to add 2 grams of charcoal for every 30 ml of water. If he adds 900 ml of water, how much charcoal does he add?"""
    # Define the ratio of charcoal to water
    CHARCOAL_PER_WATER = 2 / 30

    # Calculate the amount of charcoal needed for 900 ml of water
    charcoal_amount = CHARCOAL_PER_WATER * 900

    # Return the result
    result = charcoal_amount
    return result

print(solution())