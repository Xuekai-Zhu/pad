def solution():
    
    # Define the initial amount of chalk
    initial_chalk = 5

    # Calculate the amount of chalk used on Monday
    monday_chalk = initial_chalk * 0.2

    # Calculate the amount of chalk used on Monday after the end of the day
    monday_chalk += monday_chalk * 0.45

    # Calculate the total amount of chalk used
    total_chalk = initial_chalk + monday_chalk

    # Display the total amount of chalk used
    result = total_chalk
    return result

print(solution())