def solution():
    # Calculate the number of gumballs Hector had before giving any away
    remaining_gumballs = 6  # Hector had 6 gumballs remaining
    bobby_gumballs = (4 * alisha_gumballs) - 5  # Bobby received 5 less than 4 times as many gumballs as Alisha
    alisha_gumballs = 2 * todd_gumballs  # Alisha received twice as many gumballs as Todd
    todd_gumballs = 4 # Todd received 4 gumballs
    total_gumballs = remaining_gumballs + todd_gumballs + alisha_gumballs + bobby_gumballs

    result = total_gumballs
    return result

print(solution())