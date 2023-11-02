def solution():
    # Define the number of cans collected in the first and second week
    first_week_cans = 158
    second_week_cans = 259

    # Calculate the total number of cans collected
    total_cans = first_week_cans + second_week_cans

    # Calculate the number of cans still needed to reach the goal of 500
    cans_needed = 500 - total_cans

    result = cans_needed
    return result

print(solution())