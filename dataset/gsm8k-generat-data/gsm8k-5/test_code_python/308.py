def solution():
    charcoal_per_water = 2 / 30 # Jason needs to add 2 grams of charcoal for every 30 ml of water
    water_added = 900 # Jason adds 900 ml of water

    # Calculate the amount of charcoal needed based on the amount of water added
    charcoal_needed = charcoal_per_water * water_added
    result = charcoal_needed
    return result

print(solution())