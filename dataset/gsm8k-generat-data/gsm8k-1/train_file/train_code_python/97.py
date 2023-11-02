def solution():
    """Hector purchased a container of gumballs. He gave 4 to Todd, then he gave twice as many as he had given Todd to Alisha, and then he gave 5 less than four times as many to Bobby as he had given to Alisha. If Hector had 6 gumballs remaining, what is the total number of gumballs that Hector purchased?"""
    gumballs_given_todd = 4
    gumballs_given_alisha = gumballs_given_todd * 2
    gumballs_given_bobby = (4 * gumballs_given_alisha) - 5
    total_given_away = gumballs_given_todd + gumballs_given_alisha + gumballs_given_bobby
    total_gumballs = total_given_away + 6
    result = total_gumballs
    return result

print(solution())