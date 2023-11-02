def solution():
    """Hector purchased a container of gumballs. He gave 4 to Todd, then he gave twice as many as he had given Todd to Alisha, and then he gave 5 less than four times as many to Bobby as he had given to Alisha. If Hector had 6 gumballs remaining, what is the total number of gumballs that Hector purchased?"""
    # Define the initial number of gumballs purchased by Hector
    gumballs = None

    # Define the number of gumballs given to Todd
    gumballs_todd = 4

    # Define the number of gumballs given to Alisha
    gumballs_alisha = 2 * gumballs_todd

    # Define the number of gumballs given to Bobby
    gumballs_bobby = 4 * gumballs_alisha - 5

    # Calculate the number of remaining gumballs
    remaining_gumballs = gumballs - gumballs_todd - gumballs_alisha - gumballs_bobby

    # Solve for the initial number of gumballs
    gumballs = remaining_gumballs + 6

    result = gumballs
    return result

print(solution())