def solution():
    # Calculate the total ounces of water Kara consumes with her medication in one day
    daily_water = 4 * 3  # Kara takes one tablet three times a day and drinks 4 ounces of water with each tablet

    # Calculate the total ounces of water Kara consumes with her medication in one week
    weekly_water = daily_water * 7  # Kara takes her medication every day for a week

    # Calculate the total ounces of water Kara should consume in the second week
    second_week_water = daily_water * 6  # Kara forgot twice on one day so she only took her medication twice that day

    # Calculate the total ounces of water Kara consumed over two weeks
    total_water = weekly_water + second_week_water

    result = total_water
    return result

print(solution())