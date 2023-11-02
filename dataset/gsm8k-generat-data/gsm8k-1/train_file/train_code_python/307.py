def solution():
    """Jason is mixing a batch of black paint. He needs to add 2 grams of charcoal for every 30 ml of water. If he adds 900 ml of water, how much charcoal does he add?"""
    charcoal_per_water = 2 / 30  # grams of charcoal per ml of water
    water_amount = 900  # ml of water
    charcoal_amount = charcoal_per_water * water_amount
    result = charcoal_amount
    return result

print(solution())