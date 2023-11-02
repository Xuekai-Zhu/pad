def solution():
    # Calculate the number of men who finished the race
    men_finished = (3/4) * 80   # 1/4 of the men tripped and were unable to finish
    men_dehydrated = (2/3) * men_finished   # 2/3 of the remaining men were dehydrated
    men_finished -= (1/5) * men_dehydrated   # 1/5 of those dehydrated men couldn't finish the race
    result = men_finished
    return result

print(solution())