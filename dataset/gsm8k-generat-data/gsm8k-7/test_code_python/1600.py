def solution():
    red_bellies_percent = 0.4
    green_bellies_percent = 0.3
    red_bellies_minnows = 20

    # Calculate the percent of minnows with white bellies
    white_bellies_percent = 1 - red_bellies_percent - green_bellies_percent

    # Calculate the total number of minnows
    total_minnows = red_bellies_minnows / red_bellies_percent

    # Calculate the number of minnows with white bellies
    white_bellies_minnows = total_minnows * white_bellies_percent
    result = white_bellies_minnows
    return result

print(solution())