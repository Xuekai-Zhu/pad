def solution():
    # Find the number of yellow apples received from the neighbor
    yellow_apples = 5 * 2

    # Find the total number of apples
    total_apples = 5 + yellow_apples

    # Find the number of apples given to the son
    son_apples = total_apples * (1/5)

    # Find the remaining number of apples
    remaining_apples = total_apples - son_apples
    result = remaining_apples
    return result

print(solution())