def solution():
    points_interrupting = 5
    points_insulting = 10
    points_throwing = 25

    max_points_allowed = 100

    num_interrupting = 2
    num_insulting = 4

    # Calculate the total points Jerry has from interrupting and insulting
    total_points = (num_interrupting * points_interrupting) + (num_insulting * points_insulting)

    # Calculate the minimum number of times Jerry can throw things before reaching the maximum points allowed
    num_throwing_allowed = (max_points_allowed - total_points) // points_throwing
    result = num_throwing_allowed
    return result

print(solution())