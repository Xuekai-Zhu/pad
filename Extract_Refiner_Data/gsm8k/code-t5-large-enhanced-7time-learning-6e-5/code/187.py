def solution():
    
    # Define the amount of insects Ducks need per week
    WEEKLY_INSESSS = 3.5

    # Define the number of ducks in the flock
    NUM_DUCKS = 10

    # Calculate the total amount of insects needed per day
    total_insects = WEEKLY_INSESSS * NUM_DUCKS * 7

    # Display the total amount of insects needed per day
    result = total_insects
    return result

print(solution())