def solution():
    total_minnows = 100 # 100% of the minnows
    red_bellies = 40 # 40% of the minnows have red bellies
    green_bellies = 30 # 30% of the minnows have green bellies

    # Calculate the percentage of minnows that have white bellies
    white_bellies = 100 - red_bellies - green_bellies

    # Calculate the actual number of minnows with red bellies
    minnows_with_red = (20/40) * 100  # If 20 minnows have red bellies, that is 40% of the total minnows

    # Calculate the actual number of minnows with white bellies
    minnows_with_white = (white_bellies/100) * total_minnows - (minnows_with_red + (30/100 * total_minnows))

    result = minnows_with_white
    return result

print(solution())