def solution():
    # Calculate the total time spent cleaning up
    time_eggs = 15 * 60 * 60 / 60  # 15 seconds per egg, converted to minutes
    time_toilet_paper = 30 * 7  # 30 minutes per roll of toilet paper
    total_time = time_eggs * 60 + time_toilet_paper  # convert time_eggs to minutes and add to time_toilet_paper

    result = total_time
    return result

print(solution())