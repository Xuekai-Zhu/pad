def solution():
    # Calculate the number of paperclips Yun has after losing 12
    yun_paperclips = 20 - 12  

    # Calculate how many paperclips Marion has
    marion_paperclips = yun_paperclips * (1/4 + 1) + 7
    result = marion_paperclips
    return result

print(solution())