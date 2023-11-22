def solution():
    
    # Define the initial amount of chalk used
    initial_chalk = 5

    # Calculate the amount of chalk used after the first day
    first_day_chalk = initial_chalk * 0.2

    # Calculate the amount of chalk used after the second day
    second_day_chalk = first_day_chalk * 0.9

    # Calculate the amount of chalk used up by the end of the day
    used_up_chalk = second_day_chalk * 0.45

    # Display the amount of chalk used up by the end of the day
    result = used_up_chalk
    return result

print(solution())