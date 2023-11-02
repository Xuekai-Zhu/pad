def solution():
    """Rachel is 4 years older than Leah. If the sum of their ages is 34, how old is Rachel?"""
    # Define Leah's age as x
    x = 0

    # Calculate Rachel's age as x + 4
    rachel_age = x + 4

    # Calculate the sum of their ages as x + (x + 4) = 2x + 4
    total_age = 34

    # Solve for x: 2x + 4 = 34
    x = (total_age - 4) / 2

    # Calculate Rachel's age using x = Leah's age
    rachel_age = x + 4

    # Display Rachel's age
    result = rachel_age
    return result

print(solution())