def solution():
    """Camden went swimming 16 times in March and Susannah went 24 times. If the number of times they went throughout the month was divided equally among 4 weeks, how many more times a week did Susannah swim than Camden?"""
    # Calculate the average number of times per week each person went swimming
    camden_avg = 16 / 4
    susannah_avg = 24 / 4

    # Calculate the difference in their averages
    diff = susannah_avg - camden_avg

    # Display the difference
    result = diff
    return result

print(solution())