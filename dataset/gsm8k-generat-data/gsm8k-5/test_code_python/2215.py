def solution():
    total_men = 80  # There are 80 men in the race
    tripped_men = total_men * (1/4)  # 1/4 of the men tripped and couldn't finish
    remaining_men = total_men - tripped_men  # Calculate the number of men who didn't trip

    dehydrated_men = remaining_men * (2/3)  # 2/3 of the remaining men were dehydrated
    unable_to_finish = dehydrated_men * (1/5)  # 1/5 of the dehydrated men couldn't finish

    finished_men = remaining_men - unable_to_finish  # Calculate the number of men who finished the race
    result = finished_men
    return result

print(solution())