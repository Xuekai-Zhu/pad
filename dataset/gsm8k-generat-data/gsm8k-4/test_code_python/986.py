def solution():
    """Camden went swimming 16 times in March and Susannah went 24 times. If the number of times they went throughout the month was divided equally among 4 weeks, how many more times a week did Susannah swim than Camden?"""
    # Calculate the total number of times they went swimming
    total_swims = 16 + 24

    # Calculate the number of times they went swimming per week
    swims_per_week = total_swims / 4

    # Calculate the difference in number of times they went swimming per week
    diff = (24/4) - (16/4)

    # return the result
    result = diff
    return result

print(solution())