def solution():
    # Define the distance Carly runs each week
    week1_distance = 2
    week2_distance = 2 * week1_distance + 3
    week3_distance = (9/7) * week2_distance
    week4_distance = week3_distance - 5

    # Calculate the distance Carly ran the week she was injured
    injured_week_distance = week4_distance
    result = injured_week_distance
    return result

print(solution())