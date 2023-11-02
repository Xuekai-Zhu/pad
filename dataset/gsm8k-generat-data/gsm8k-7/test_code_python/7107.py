def solution():
    num_bags = 3

    # Calculate the total number of jelly beans in the fishbowl
    total_jelly_beans = num_bags * (24 + 13 + 36 + 28 + 32 + 18)

    # Calculate the percentage of jelly beans that are red or white
    red_white_percent = (24 + 18) / total_jelly_beans

    # Calculate the number of red or white jelly beans in the fishbowl
    red_white_jelly_beans = int(round(red_white_percent * total_jelly_beans))

    result = red_white_jelly_beans
    return result

print(solution())