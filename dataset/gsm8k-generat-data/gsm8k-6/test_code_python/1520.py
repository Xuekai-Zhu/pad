def solution():
    # Calculate the total number of cookies eaten by Monica's family
    total_eaten = 10 + (1/2)*10 + 2  # father ate 10 cookies, mother ate half as much as the father, brother ate 2 more than mother
    
    # Calculate the number of cookies left for Monica
    cookies_left = 30 - total_eaten
    result = cookies_left
    return result

print(solution())