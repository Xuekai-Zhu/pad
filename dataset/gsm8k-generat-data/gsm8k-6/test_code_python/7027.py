def solution():
    # Calculate the miles run by Bob on day one and day two
    day_one_miles = 0.2 * 70  # Bob runs 20 percent of the total miles on day one
    remaining_miles = 70 - day_one_miles
    day_two_miles = 0.5 * remaining_miles  # Bob runs 50 percent of the remaining miles on day two

    # Calculate the miles run by Bob on day three
    day_three_miles = 70 - day_one_miles - day_two_miles
    result = day_three_miles
    return result

print(solution())