def solution():
    # Calculate the total number of jelly beans in one bag
    total_jelly_beans = sum([24, 13, 36, 28, 32, 18])
    
    # Calculate the ratio of red and white jelly beans in one bag
    red_and_white_ratio = (24 + 18) / total_jelly_beans
    
    # Calculate the total number of jelly beans in three bags
    total_jelly_beans_in_fishbowl = total_jelly_beans * 3
    
    # Calculate the estimated number of red and white jelly beans in the fishbowl
    red_and_white_jelly_beans_est = total_jelly_beans_in_fishbowl * red_and_white_ratio
    
    result = red_and_white_jelly_beans_est
    return result

print(solution())