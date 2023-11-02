def solution():
    num_tennis_balls = 15
    num_soccer_balls = 5
    num_baskets = 5
    num_students = 5
    balls_removed_by_3_students = 8

    # Calculate the total number of tennis balls and soccer balls in all baskets
    total_balls = (num_tennis_balls + num_soccer_balls) * num_baskets

    # Calculate the total number of balls removed by the first 3 students
    balls_removed_by_first_3_students = balls_removed_by_3_students * 3

    # Calculate the total number of balls remaining in the baskets
    balls_remaining = total_balls - balls_removed_by_first_3_students - 56

    # Calculate the total number of balls removed by the other 2 students
    balls_removed_by_other_students = balls_remaining / 2
    result = balls_removed_by_other_students
    return result

print(solution())