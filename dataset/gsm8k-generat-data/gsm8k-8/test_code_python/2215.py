def solution():
    # Calculate the number of men who tripped and couldn't finish
    tripped_men = 80 * (1/4)

    # Calculate the number of remaining men
    remaining_men = 80 - tripped_men

    # Calculate the number of dehydrated men
    dehydrated_men = remaining_men * (2/3)

    # Calculate the number of dehydrated men who couldn't finish
    unable_to_finish = dehydrated_men * (1/5)

    # Calculate the number of men who finished the race
    finished_race = remaining_men - unable_to_finish
    result = finished_race
    return result

print(solution())