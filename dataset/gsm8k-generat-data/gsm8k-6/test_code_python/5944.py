def solution():
    # Calculate the total number of corn cobs and potatoes before the pests destroyed the crops
    corn_cobs = 9 * 10  # 10 rows of corn stalks producing 9 corn cobs each
    potatoes = 30 * 5  # 5 rows of potatoes producing 30 potatoes each

    # Calculate the number of crops remaining after half of them were destroyed by pests
    remaining_crops = (corn_cobs + potatoes) // 2

    result = remaining_crops
    return result

print(solution())