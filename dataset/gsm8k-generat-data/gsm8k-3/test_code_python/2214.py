def solution():
    """Matt did his homework for 150 minutes. He spent 30% of that time on math and 40% on science. He spent the remaining time on other subjects. How much time did Matt spend on homework in other subjects?"""
    # Define the total time spent on homework
    total_time = 150

    # Calculate the time spent on math
    math_time = total_time * 0.3

    # Calculate the time spent on science
    science_time = total_time * 0.4

    # Calculate the time spent on other subjects
    other_time = total_time - math_time - science_time

    # Display the time spent on other subjects
    result = other_time
    return result

print(solution())