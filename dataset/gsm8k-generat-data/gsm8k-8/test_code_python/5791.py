def solution():
    # Define the amount earned per mile last year and this year
    earnings_per_mile_last_year = 4
    earnings_per_mile_this_year = 2.75

    # Define the amount collected by last year's winner
    amount_collected_last_year = 44

    # Calculate the number of miles last year's winner walked
    miles_walked_last_year = amount_collected_last_year / earnings_per_mile_last_year

    # Calculate the number of miles Elroy needs to walk to collect the same amount of money
    miles_needed_to_collec_same_amount = amount_collected_last_year / earnings_per_mile_this_year

    # Calculate the difference in miles between Elroy and last year's winner
    difference_in_miles = miles_needed_to_collec_same_amount - miles_walked_last_year
    result = difference_in_miles
    return result

print(solution())