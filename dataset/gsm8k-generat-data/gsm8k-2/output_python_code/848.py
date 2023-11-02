def solution():
    """A hot air balloon with 200 balloons is blowing up. After about half an hour, 1/5 of the total number of balloons in the hot air balloon have blown up. After another hour, twice the number of balloons that had already blown up also blow up. How many balloons in the hot air balloon remain intact?"""
    total_balloons = 200
    first_half_hour_balloons_blown = total_balloons / 5
    remaining_balloons = total_balloons - first_half_hour_balloons_blown
    second_hour_balloons_blown = 2 * first_half_hour_balloons_blown
    remaining_balloons -= second_hour_balloons_blown
    result = remaining_balloons
    return result

print(solution())