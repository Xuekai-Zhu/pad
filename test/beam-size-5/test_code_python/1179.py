def solution():
    
    # Define the initial number of apples
    initial_apples = 0

    # Newton picked up the first two apples
    first_two_apples = initial_apples - 1

    # Newton picked up the second two apples
    second_two_apples = second_two_apples - 5

    # Newton picked up the third two apples
    third_two_apples = second_two_apples - 6

    # Total number of apples
    total_apples = first_two_apples + second_two_apples + third_two_apples

    # Display the total number of apples
    result = total_apples
    return result

print(solution())