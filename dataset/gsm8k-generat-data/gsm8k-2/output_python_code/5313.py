def solution():
    """A coach placed 15 tennis balls and 5 soccer balls each into 5 baskets. He gave 5 of his students a short period of time to remove as many balls each from a basket as they could. 3 of them removed 8 balls each and the other 2 removed a certain number of balls each. If a total of 56 balls are still in the baskets, how many balls did the other 2 students each remove?"""
    total_baskets = 5
    total_tennis_balls = 15 * total_baskets
    total_soccer_balls = 5 * total_baskets
    total_initial_balls = total_tennis_balls + total_soccer_balls
    balls_removed = 3 * 8
    remaining_balls = total_initial_balls - balls_removed - 56
    balls_removed_by_other_students = remaining_balls / 2
    result = balls_removed_by_other_students
    return result

print(solution())