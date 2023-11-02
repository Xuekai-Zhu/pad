def solution():
    """Eliana walked 200 steps for her morning exercise, did some press-ups, then added some 300 more steps to her count for the first day. The next day, she walked twice the number of steps she walked on the first day. And on the third day, Eliana walked an additional 100 steps. What's the total number of steps Eliana walked during these three days?"""
    # Calculate the steps for day one
    day_one = 200 + 300

    # Calculate the steps for day two
    day_two = day_one * 2

    # Calculate the steps for day three
    day_three = day_two + 100

    # Calculate the total steps for the three days
    total_steps = day_one + day_two + day_three

    # return the result
    result = total_steps
    return result

print(solution())