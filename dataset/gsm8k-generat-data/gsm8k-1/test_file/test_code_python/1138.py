def solution():
    """Jess is trying to guess the number of blue jellybeans in a jar. She can see that there are 17 green jelly beans and twice as many red jelly beans. The rest of the jellybeans are blue jelly beans. If there are a total of 60 jelly beans in total, how many blue jellybeans are there?"""
    green_jellybeans = 17
    red_jellybeans = 2 * green_jellybeans
    total_jellybeans = 60
    blue_jellybeans = total_jellybeans - (green_jellybeans + red_jellybeans)
    result = blue_jellybeans
    return result

print(solution())