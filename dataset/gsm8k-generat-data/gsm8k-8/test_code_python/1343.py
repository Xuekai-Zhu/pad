def solution():
    # Define the total number of shoes and the number of blue shoes
    total_shoes = 1250
    blue_shoes = 540

    # Calculate the number of green shoes
    green_shoes = (total_shoes - blue_shoes) / 2

    # Calculate the number of purple shoes
    purple_shoes = green_shoes

    result = purple_shoes
    return result

print(solution())