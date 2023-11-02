def solution():
    eggs = 60  # The number of eggs the house will need to clean up
    toilet_paper = 7  # The number of rolls of toilet paper the house will need to clean up
    egg_cleaning_time = 15/60  # The time it takes to clean up one egg in minutes
    toilet_paper_cleaning_time = 30  # The time it takes to clean up one roll of toilet paper in minutes

    # Calculate the total time it will take to clean up all the eggs and toilet paper
    total_time = (eggs * egg_cleaning_time) + (toilet_paper * toilet_paper_cleaning_time)
    result = total_time
    return result

print(solution())