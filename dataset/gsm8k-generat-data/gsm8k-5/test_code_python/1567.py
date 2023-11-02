def solution():
    # Calculate the total miles run by Billy in the first three days
    billy_miles_first_three_days = 1 + 1 + 1

    # Calculate the total miles run by Tiffany in the first three days
    tiffany_miles_first_three_days = 2 + 2 + 2

    # Calculate the total miles run by Billy in the last three days
    billy_miles_last_three_days = 1 + 1 + 1

    # Calculate the total miles run by Tiffany in the last three days
    tiffany_miles_last_three_days = 1/3 + 1/3 + 1/3

    # Calculate the total miles run by Tiffany in the week
    tiffany_total_miles = tiffany_miles_first_three_days + tiffany_miles_last_three_days

    # Calculate the miles Billy needs to run on Saturday to tie Tiffany
    billy_total_miles_needed = tiffany_total_miles - (billy_miles_first_three_days + billy_miles_last_three_days)

    result = billy_total_miles_needed
    return result

print(solution())