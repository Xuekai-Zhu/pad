def solution():
    # Calculate the total number of ounces in the pot of soup
    total_ounces = 6 * 128  # 6 gallons, each gallon has 128 ounces

    # Calculate the total number of bowls of soup
    total_bowls = total_ounces / 10  # Each bowl has 10 ounces

    # Calculate the time it will take Erin to serve all the soup
    time_in_minutes = total_bowls / 5  # Erin can serve 5 bowls per minute

    # Round the time to the nearest minute
    rounded_time = round(time_in_minutes)

    result = rounded_time
    return result

print(solution())