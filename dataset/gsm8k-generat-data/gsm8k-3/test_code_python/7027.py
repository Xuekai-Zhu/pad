def solution():
    """Bob, a marathon runner, is preparing for a race.  He runs a total of 70 miles in the 3 days leading up to the race. On day one he runs 20 percent of the total miles and on day 2 he runs 50 percent of the remaining miles.  How many miles does he run on day three to complete the 70 miles?"""
    # Define the total number of miles Bob runs
    total_miles = 70

    # Calculate the number of miles Bob runs on day 1
    day1_miles = total_miles * 0.2

    # Calculate the number of miles Bob has left to run after day 1
    remaining_miles1 = total_miles - day1_miles

    # Calculate the number of miles Bob runs on day 2
    day2_miles = remaining_miles1 * 0.5

    # Calculate the number of miles Bob has left to run after day 2
    remaining_miles2 = remaining_miles1 - day2_miles

    # Calculate the number of miles Bob runs on day 3
    day3_miles = remaining_miles2

    # Display the number of miles Bob runs on day 3
    result = day3_miles
    return result

print(solution())