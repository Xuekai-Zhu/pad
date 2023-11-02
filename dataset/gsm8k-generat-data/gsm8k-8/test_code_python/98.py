def solution():
    total_gumballs = 0
    remaining_gumballs = 6

    # Calculate how many gumballs Hector had before giving any away
    total_gumballs += remaining_gumballs
    remaining_gumballs += 4

    # Calculate how many gumballs Hector gave to Alisha
    alisha_gumballs = 2 * 4
    remaining_gumballs -= alisha_gumballs
    total_gumballs += alisha_gumballs

    # Calculate how many gumballs Hector gave to Bobby
    bobby_gumballs = 4 * alisha_gumballs - 5
    remaining_gumballs -= bobby_gumballs
    total_gumballs += bobby_gumballs

    # Calculate the total number of gumballs Hector purchased
    total_gumballs += remaining_gumballs

    result = total_gumballs
    return result

print(solution())