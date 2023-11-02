def solution():
    bakery1 = 2  # First bakery needs 2 sacks per week
    bakery2 = 4  # Second bakery needs 4 sacks per week
    bakery3 = 12  # Third bakery needs 12 sacks per week
    weeks = 4  # Antoine wants to supply the bakeries for 4 weeks

    # Calculate the total number of sacks needed for all three bakeries
    total_sacks_needed = bakery1 + bakery2 + bakery3

    # Calculate the total number of sacks needed for all three bakeries in 4 weeks
    total_sacks_needed_4_weeks = total_sacks_needed * weeks
    result = total_sacks_needed_4_weeks
    return result

print(solution())