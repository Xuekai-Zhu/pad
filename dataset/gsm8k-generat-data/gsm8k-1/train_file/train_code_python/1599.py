def solution():
    """Mary is counting the number of minnows in the pond. 40% of the minnows have red bellies, 30% have green bellies and the rest have white bellies. If 20 minnows have red bellies, how many minnows have white bellies?"""
    total_minnows = 100  # assume total number of minnows is 100
    red_minnows = 40   # 40% of minnows have red bellies
    green_minnows = 30   # 30% of minnows have green bellies
    white_minnows = 100 - (red_minnows + green_minnows)   # rest of the minnows would have white bellies
    red_minnows_count = 20   # given that 20 minnows have red bellies
    white_minnows_count = (white_minnows/60) * 20   # calculating the count of minnows with white bellies
    result = white_minnows_count
    return result

print(solution())