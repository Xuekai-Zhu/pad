def solution():
    # Calculate the total time John spends watching cartoons and doing chores
    total_time = 2 * 60  # John watches cartoons for 2 hours
    cartoon_time = total_time  # John watches cartoons for the entire 2 hours
    chore_time = (cartoon_time // 10) * 8  # For every 10 minutes of cartoons, he has to do 8 minutes of chores

    result = chore_time
    return result

print(solution())