def solution():
    # Fill the 5-liter bucket and pour into the 3-liter bucket
    remaining_water = 5 - 3  

    # Pour the remaining water into the 6-liter bucket
    remaining_volume = 6 - remaining_water  

    result = remaining_volume  # The remaining volume is the max amount she can put into the 6-liter bucket without overflowing
    return result

print(solution())