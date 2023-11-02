def solution():
    # Calculate the total number of balls in the baskets
    total_balls = (15 + 5) * 5

    # Calculate the total number of balls removed by the first 3 students
    balls_removed_by_first_three = 3 * 8

    # Calculate the number of balls removed by the other 2 students
    balls_removed_by_other_two = total_balls - balls_removed_by_first_three - 56
    balls_removed_by_each_other_two = balls_removed_by_other_two / 2

    result = balls_removed_by_each_other_two
    return result

print(solution())