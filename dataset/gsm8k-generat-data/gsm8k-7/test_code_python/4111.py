def solution():
    kidney_apples = 23
    golden_apples = 37
    canada_apples = 14
    sold_apples = 36

    # Calculate the total mass of apples on the shelves
    total_apples = kidney_apples + golden_apples + canada_apples

    # Calculate the mass of apples left after selling
    remaining_apples = total_apples - sold_apples
    result = remaining_apples
    return result

print(solution())