def solution():
    """A hot air balloon with 200 balloons is blowing up. After about half an hour, 1/5 of the total number of balloons in the hot air balloon have blown up. After another hour, twice the number of balloons that had already blown up also blow up. How many balloons in the hot air balloon remain intact?"""
    total_balloons = 200
    half_hour_burst = total_balloons // 5
    remaining_balloons = total_balloons - half_hour_burst
    two_hour_burst = (half_hour_burst * 2)
    remaining_balloons = remaining_balloons - two_hour_burst
    result = remaining_balloons
    return result

print(solution())