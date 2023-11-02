def solution():
    # Calculate the total points scored in the first 20 minutes
    first_20_points = 4

    # Calculate the total points scored in the second 20 minutes
    second_20_points = 1.25 * first_20_points

    # Calculate the total points scored in the first 20 minutes
    first_20_total_points = first_20_points + second_20_points

    # Calculate the total points scored in the second 20 minutes
    second_20_total_points = first_20_points + second_20_points

    # Calculate the total points scored
    total_points = first_20_total_points + second_20_total_points
    result = total_points
    return result

print(solution())