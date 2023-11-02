def solution():
    """There are 14 kindergartners and 24 first graders and some second graders in Ms. Watson's class. Overall Ms. Watson has 42 students. How many second graders are in Ms. Watson’s class?"""
    # Define the number of kindergartners and first graders
    kindergartners = 14
    first_graders = 24

    # Calculate the number of second graders
    second_graders = 42 - kindergartners - first_graders

    # Display the number of second graders
    result = second_graders
    return result

print(solution())