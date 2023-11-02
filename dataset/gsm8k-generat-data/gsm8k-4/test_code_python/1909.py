def solution():
    """40 kids are running a race. 10% of them pass the finish line in less than 6 minutes. Three times that number finish in less than 8 minutes. 1/6 of the remaining kids take more than 14 minutes. How many kids take more than 14 minutes?"""
    # Define the initial number of kids
    total_kids = 40

    # Calculate the number of kids who finish in less than 6 minutes
    less_than_6 = total_kids * 0.1

    # Calculate the number of kids who finish between 6 and 8 minutes
    between_6_and_8 = less_than_6 * 3

    # Calculate the number of remaining kids
    remaining_kids = total_kids - less_than_6 - between_6_and_8

    # Calculate the number of kids who take more than 14 minutes
    more_than_14 = remaining_kids / 6

    result = more_than_14
    return result

print(solution())