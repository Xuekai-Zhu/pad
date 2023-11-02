def solution():
    """The school nurse must conduct lice checks at the elementary school. She must check 26 Kindergarteners, 19 first graders, 20 second graders, and 25 third graders. If each check takes 2 minutes, how many hours will it take the nurse to complete all the checks?"""
    # Define the number of students in each grade
    KINDERGARTENERS = 26
    FIRST_GRADERS = 19
    SECOND_GRADERS = 20
    THIRD_GRADERS = 25

    # Define the time it takes to check each student
    CHECK_TIME = 2 # minutes

    # Calculate the total number of checks
    total_checks = KINDERGARTENERS + FIRST_GRADERS + SECOND_GRADERS + THIRD_GRADERS

    # Calculate the total time in minutes
    total_time = total_checks * CHECK_TIME

    # Convert to hours
    hours = total_time / 60

    # Display the total time in hours
    result = hours
    return result

print(solution())