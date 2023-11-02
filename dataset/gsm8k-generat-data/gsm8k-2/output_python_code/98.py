def solution():
    """Hector purchased a container of gumballs. He gave 4 to Todd, then he gave twice as many as he had given Todd to Alisha, and then he gave 5 less than four times as many to Bobby as he had given to Alisha. If Hector had 6 gumballs remaining, what is the total number of gumballs that Hector purchased?"""
    todd_gumballs = 4
    alisha_gumballs = 2 * todd_gumballs
    bobby_gumballs = 4 * alisha_gumballs - 5
    total_gumballs = todd_gumballs + alisha_gumballs + bobby_gumballs + 6
    result = total_gumballs
    return result

print(solution())