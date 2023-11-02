def solution():
    # Calculate the total number of minnows with red bellies
    red_bellies = 20

    # Calculate the percentage of minnows with white bellies
    white_bellies_percent = 100 - 40 - 30

    # Calculate the total number of minnows
    total_minnows = (red_bellies / 0.4)

    # Calculate the total number of minnows with white bellies
    white_bellies = total_minnows * (white_bellies_percent / 100)

    result = white_bellies
    return result

print(solution())