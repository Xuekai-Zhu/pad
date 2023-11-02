def solution():
    """There are 80 men in a race. 1/4 of the men tripped and were unable to finish. 2/3 of the remaining men were dehydrated and 1/5 of those dehydrated men couldn't finish the race. How many men finished the race?"""
    # Define the initial number of men
    initial_men = 80

    # Calculate the number of men who tripped and could not finish
    tripped_men = initial_men // 4

    # Calculate the number of men remaining after the tripped men
    remaining_men = initial_men - tripped_men

    # Calculate the number of dehydrated men
    dehydrated_men = remaining_men * (2 / 3)

    # Calculate the number of dehydrated men who could not finish
    unable_to_finish = dehydrated_men * (1 / 5)

    # Calculate the number of men who finished the race
    finished_men = remaining_men - unable_to_finish

    # Return the result
    result = finished_men
    return result

print(solution())