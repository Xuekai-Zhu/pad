def solution():
    levi_score = 8
    brother_score = 12
    brother_extra_score = 3
    goal_difference = 5

    # Calculate the current difference in scores
    current_difference = brother_score - levi_score

    # Calculate the target difference in scores
    target_difference = goal_difference + brother_extra_score

    # Calculate the number of times Levi needs to score to reach his goal
    needed_score = target_difference - current_difference
    result = needed_score
    return result

print(solution())