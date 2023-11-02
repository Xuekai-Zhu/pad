def solution():
    # Calculate the height of the corn plant after 3 weeks
    first_week_growth = 2
    second_week_growth = 2 * first_week_growth
    third_week_growth = 4 * second_week_growth
    total_growth = first_week_growth + second_week_growth + third_week_growth
    height_now = 2 + total_growth  # the plant was 2 inches tall after the first week
    result = height_now
    return result

print(solution())