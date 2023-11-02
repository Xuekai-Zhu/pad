def solution():
    """A phone tree is used to contact families and relatives of Ali's deceased coworker. Ali decided to call 3 families. Then each family calls 3 other families, and so on. How many families will be notified during the fourth round of calls?"""
    initial_families = 3
    round_one_families = initial_families * 3
    round_two_families = round_one_families * 3
    round_three_families = round_two_families * 3
    round_four_families = round_three_families * 3
    result = round_four_families
    return result

print(solution())