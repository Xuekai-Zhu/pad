def solution():
    vietnamese_height = 64.74 # convert height to inches
    nba_height = 79 # convert height to inches
    if vietnamese_height < nba_height:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())