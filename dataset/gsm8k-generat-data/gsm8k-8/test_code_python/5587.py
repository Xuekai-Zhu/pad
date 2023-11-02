def solution():
    # Calculate the number of yellow apples
    yellow_apples = 2 * 5

    # Calculate the total number of apples
    total_apples = 5 + yellow_apples

    # Calculate the number of apples given to son
    son_apples = total_apples * 1/5

    # Calculate the remaining number of apples
    remaining_apples = total_apples - son_apples

    result = remaining_apples
    return result

print(solution())