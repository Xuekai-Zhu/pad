def solution():
    # Calculate the total number of corn cobs
    total_corn_cobs = 9 * 10  # 10 rows of corn stalks, each producing 9 corn cobs

    # Calculate the total number of potatoes
    total_potatoes = 30 * 5  # 5 rows of potatoes, each producing 30 potatoes

    # Calculate the total number of crops before the pest damage
    total_crops_before = total_corn_cobs + total_potatoes

    # Calculate the total number of crops after the pest damage
    total_crops_after = total_crops_before / 2  # Half of the crops were destroyed by pests

    result = total_crops_after
    return result

print(solution())