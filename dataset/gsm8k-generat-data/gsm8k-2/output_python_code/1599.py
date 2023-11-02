def solution():
    """Mary is counting the number of minnows in the pond. 40% of the minnows have red bellies, 30% have green bellies and the rest have white bellies. If 20 minnows have red bellies, how many minnows have white bellies?"""
    red_bellies = 20
    total_minnows = 100  # assuming a total of 100%
    green_bellies = 30
    white_bellies = total_minnows - red_bellies - green_bellies
    white_bellies_percentage = 100 - red_bellies - green_bellies
    white_bellies_count = (white_bellies_percentage * total_minnows) / 100
    result = white_bellies_count
    return result

print(solution())