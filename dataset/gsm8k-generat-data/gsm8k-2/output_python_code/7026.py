def solution():
    """Bob, a marathon runner, is preparing for a race. He runs a total of 70 miles in the 3 days leading up to the race. On day one he runs 20 percent of the total miles and on day 2 he runs 50 percent of the remaining miles. How many miles does he run on day three to complete the 70 miles?"""
    total_miles = 70
    day1_miles = 0.2 * total_miles
    remaining_miles = total_miles - day1_miles
    day2_miles = 0.5 * remaining_miles
    day3_miles = total_miles - day1_miles - day2_miles
    result = day3_miles
    return result

print(solution())