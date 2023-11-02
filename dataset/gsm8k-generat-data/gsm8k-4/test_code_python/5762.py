def solution():
    """The school nurse must conduct lice checks at the elementary school. She must check 26 Kindergarteners, 19 first graders, 20 second graders, and 25 third graders. If each check takes 2 minutes, how many hours will it take the nurse to complete all the checks?"""
    # Define the number of students in each grade and the time per check
    KINDERGARTENERS = 26
    FIRST_GRADERS = 19
    SECOND_GRADERS = 20
    THIRD_GRADERS = 25
    TIME_PER_CHECK = 2

    # Calculate the total number of checks and the time needed to complete them
    total_checks = KINDERGARTENERS + FIRST_GRADERS + SECOND_GRADERS + THIRD_GRADERS
    total_time = total_checks * TIME_PER_CHECK

    # Convert the time to hours
    hours = total_time / 60

    # return the result rounded to 2 decimal points
    result = round(hours, 2)
    return result

print(solution())