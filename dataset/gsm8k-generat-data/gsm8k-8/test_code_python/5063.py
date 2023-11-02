def solution():
    # Calculate the total number of pages used per week
    pages_per_week = 2 * 5 * 5

    # Calculate the total number of pages used after 6 weeks
    pages_after_6_weeks = pages_per_week * 6

    # Calculate the total number of packs of paper needed
    packs_needed = (pages_after_6_weeks / 100) + 1

    result = packs_needed
    return result

print(solution())