def solution():
    starting_amount = 6  # Hector had 6 gumballs remaining at the end
    todd_amount = 4  # Hector gave 4 gumballs to Todd
    alisha_amount = 2 * todd_amount  # Hector gave twice as many gumballs to Alisha as he gave to Todd
    bobby_amount = 4 * alisha_amount - 5  # Hector gave 5 less than four times as many gumballs to Bobby as he gave to Alisha

    # Calculate the total number of gumballs Hector purchased
    total_gumballs = starting_amount + todd_amount + alisha_amount + bobby_amount
    result = total_gumballs
    return result

print(solution())