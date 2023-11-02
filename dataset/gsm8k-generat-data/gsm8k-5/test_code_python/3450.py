def solution():
    # Calculate the time it takes Carson to mow the lawn
    mow_time = 40 * 2  # 2 minutes to mow one line, 40 lines in total

    # Calculate the time it takes Carson to plant the flowers
    flowers_planted = 8 * 7  # 8 rows with 7 flowers each
    plant_time = flowers_planted * 0.5  # Half a minute to plant each flower

    # Calculate the total time Carson spends gardening
    total_time = mow_time + plant_time
    result = total_time
    return result

print(solution())