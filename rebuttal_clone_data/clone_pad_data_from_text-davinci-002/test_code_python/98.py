def solution():
    """Hector purchased a container of gumballs. He gave 4 to Todd, then he gave twice as many as he had given Todd to Alisha, and then he gave 5 less than four times as many to Bobby as he had given to Alisha. If Hector had 6 gumballs remaining, what is the total number of gumballs that Hector purchased?"""
    gumballs_given_to_todd = 4
    gumballs_given_to_alisha = 2 * gumballs_given_to_todd
    gumballs_given_to_bobby = (4 * gumballs_given_to_alisha) - 5
    gumballs_remaining = 6
    total_gumballs = gumballs_given_to_todd + gumballs_given_to_alisha + gumballs_given_to_bobby + gumballs_remaining
    result = total_gumballs
    return result

print(solution())