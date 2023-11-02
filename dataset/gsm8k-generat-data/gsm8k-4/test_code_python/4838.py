def solution():
    """Six Grade 4 sections launched a recycling drive where they collect old newspapers to recycle. Each section collected 280 kilos in two weeks. After the third week, they found that they need 320 kilos more to reach their target. How many kilos of the newspaper is their target?"""
    # Define the number of sections and the amount of newspapers collected in two weeks
    sections = 6
    newspapers_per_section = 280

    # Calculate the total amount of newspapers collected in two weeks
    total_newspapers = sections * newspapers_per_section

    # Calculate the amount of newspapers collected in three weeks
    newspapers_after_three_weeks = total_newspapers * 3 / 2

    # Calculate the target amount of newspapers
    target_newspapers = newspapers_after_three_weeks + 320

    # return the result
    result = target_newspapers
    return result

print(solution())