def solution():
    """Tate finishes high school in 1 year less than normal. It takes him 3 times that long to get his bachelor's degree and Ph.D. How many years did he spend in high school and college?"""
    # Define the time spent in high school as x
    x = 0

    # Define the time spent in college (bachelor's and Ph.D.) as 3x
    college_time = 3 * x

    # Define the total time spent in school as high school time plus college time
    total_time = x + college_time

    # Since Tate finishes high school in 1 year less than normal, we can set x to be 1 less than the normal high school time, which is 4 years
    x = 4 - 1

    # Calculate the time spent in college
    college_time = 3 * x

    # Calculate the total time
    total_time = x + college_time

    # Return the result as a tuple of (high school time, college time)
    result = (x, college_time)
    return result

print(solution())