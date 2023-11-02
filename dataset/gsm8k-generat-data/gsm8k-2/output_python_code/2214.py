def solution():
    """There are 80 men in a race. 1/4 of the men tripped and were unable to finish. 2/3 of the remaining men were dehydrated and 1/5 of those dehydrated men couldn't finish the race. How many men finished the race?"""
    total_men = 80
    tripped_men = total_men * 0.25
    remaining_men = total_men - tripped_men
    dehydrated_men = remaining_men * (2/3)
    unable_to_finish = dehydrated_men * 0.2
    finished_men = remaining_men - dehydrated_men + unable_to_finish
    result = finished_men
    return result

print(solution())