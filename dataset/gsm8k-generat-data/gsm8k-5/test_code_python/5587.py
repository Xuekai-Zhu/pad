def solution():
    blue_apples = 5  # I have 5 blue apples
    yellow_apples = 2 * blue_apples  # My neighbor gives me twice as many yellow apples as I have blue ones
    total_apples = blue_apples + yellow_apples  # The total number of apples I have now
    son_apples = total_apples / 5  # I give my son 1/5 of the total number of apples

    # Calculate the remaining number of apples
    remaining_apples = total_apples - son_apples
    result = remaining_apples
    return result

print(solution())