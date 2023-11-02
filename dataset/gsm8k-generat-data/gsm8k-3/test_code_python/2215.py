def solution():
    """There are 80 men in a race. 1/4 of the men tripped and were unable to finish. 2/3 of the remaining men were dehydrated and 1/5 of those dehydrated men couldn't finish the race. How many men finished the race?"""
    # Define the total number of men in the race
    total_men = 80

    # Calculate the number of men who tripped and couldn't finish
    tripped_men = total_men // 4

    # Calculate the number of men who finished the race
    finished_men = total_men - tripped_men

    # Calculate the number of dehydrated men
    dehydrated_men = (2/3) * finished_men

    # Calculate the number of dehydrated men who couldn't finish
    unable_to_finish = (1/5) * dehydrated_men

    # Calculate the number of men who finished the race
    actual_finishers = finished_men - unable_to_finish

    # Display the number of men who finished the race
    result = actual_finishers
    return result

print(solution())