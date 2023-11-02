def solution():
    # Define the number of blue, purple, and orange jellybeans
    blue_jellybeans = 14
    purple_jellybeans = 26
    orange_jellybeans = 40

    # Calculate the total number of jellybeans
    total_jellybeans = 200

    # Determine the total number of red jellybeans by subtracting the other colors from the total
    red_jellybeans = total_jellybeans - blue_jellybeans - purple_jellybeans - orange_jellybeans
    result = red_jellybeans
    return result

print(solution())