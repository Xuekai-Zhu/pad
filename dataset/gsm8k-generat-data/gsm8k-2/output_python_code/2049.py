def solution():
    """John attends a protest for 4 days. He then attends a second protest for 25% longer than the first. How many days did he spend protesting?"""
    first_protest_days = 4
    second_protest_days = 1.25 * first_protest_days
    total_days = first_protest_days + second_protest_days
    result = total_days
    return result

print(solution())