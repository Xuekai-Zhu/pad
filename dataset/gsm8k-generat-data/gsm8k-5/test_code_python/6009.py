def solution():
    red_roses = 0.5 * 12  # Lorelei picks 50% of the red roses
    pink_roses = 0.5 * 18  # Lorelei picks 50% of the pink roses
    yellow_roses = 0.25 * 20  # Lorelei picks 25% of the yellow roses
    orange_roses = 0.25 * 8  # Lorelei picks 25% of the orange roses

    # Calculate the total number of roses in Lorelei's vase
    total_roses = red_roses + pink_roses + yellow_roses + orange_roses
    result = total_roses
    return result

print(solution())