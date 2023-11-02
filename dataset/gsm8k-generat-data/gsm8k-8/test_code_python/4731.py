def solution():
    # Define the variables
    total_apples = 20
    monday_apples = 2
    thursday_apples = 4 * friday_apples
    friday_apples = 0.5 * monday_apples

    # Calculate the remaining apples from Tuesday, Thursday, and Friday
    remaining_apples = total_apples - monday_apples - thursday_apples - friday_apples

    # Calculate the apples eaten on Wednesday
    wednesday_apples = remaining_apples
    result = wednesday_apples
    return result

print(solution())