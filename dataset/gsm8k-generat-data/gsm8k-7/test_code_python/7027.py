def solution():
    total_miles = 70
    day_one_percent = 0.2
    day_two_percent = 0.5

    # Calculate the number of miles Bob runs on day one
    day_one_miles = total_miles * day_one_percent

    # Calculate the remaining miles after day one
    remaining_miles = total_miles - day_one_miles

    # Calculate the number of miles Bob runs on day two
    day_two_miles = remaining_miles * day_two_percent

    # Calculate the number of miles Bob runs on day three
    day_three_miles = total_miles - day_one_miles - day_two_miles
    result = day_three_miles
    return result

print(solution())