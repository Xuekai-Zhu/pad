def solution():
    # Calculate the number of each type of rose that Lorelei picks
    red_roses = 12 * 0.5  # 50% of the red roses
    pink_roses = 18 * 0.5  # 50% of the pink roses
    yellow_roses = 20 * 0.25  # 25% of the yellow roses
    orange_roses = 8 * 0.25  # 25% of the orange roses

    # Calculate the total number of roses in Lorelei's vase
    total_roses = red_roses + pink_roses + yellow_roses + orange_roses
    result = total_roses
    return result

print(solution())