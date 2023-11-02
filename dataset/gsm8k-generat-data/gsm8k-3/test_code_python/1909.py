def solution():
    """40 kids are running a race. 10% of them pass the finish line in less than 6 minutes. Three times that number finish in less than 8 minutes. 1/6 of the remaining kids take more than 14 minutes. How many kids take more than 14 minutes?"""
    # Define the total number of kids in the race
    total_kids = 40

    # Calculate the number of kids who finish in less than 6 minutes
    less_than_6 = total_kids * 0.1

    # Calculate the number of kids who finish in less than 8 minutes
    less_than_8 = less_than_6 * 3

    # Calculate the number of kids who take more than 8 minutes
    more_than_8 = total_kids - less_than_6 - less_than_8

    # Calculate the number of kids who take more than 14 minutes
    more_than_14 = more_than_8 * (1/6)

    # Display the number of kids who take more than 14 minutes
    result = more_than_14
    return result

print(solution())