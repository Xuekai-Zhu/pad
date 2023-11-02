def solution():
    points_for_interrupting = 5
    points_for_insulting = 10
    points_for_throwing = 25
    points_to_office = 100
    Jerry_points = 2 * points_for_interrupting + 4 * points_for_insulting
    points_remaining = points_to_office - Jerry_points
    times_can_throw = points_remaining // points_for_throwing
    result = times_can_throw
    return result

print(solution())