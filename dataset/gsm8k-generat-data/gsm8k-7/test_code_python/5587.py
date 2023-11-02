def solution():
    num_blue_apples = 5

    # Calculate the number of yellow apples the neighbor gives
    num_yellow_apples = num_blue_apples * 2

    # Calculate the total number of apples
    total_apples = num_blue_apples + num_yellow_apples

    # Calculate the number of apples given to the son
    num_apples_given = total_apples / 5

    # Calculate the remaining number of apples
    num_remaining_apples = total_apples - num_apples_given
    result = num_remaining_apples
    return result

print(solution())