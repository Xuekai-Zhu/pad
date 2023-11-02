def solution():
    # Define the final score and the number of field goals
    final_score = 37
    field_goals = 3

    # Calculate the score from touchdowns
    touchdown_score = final_score - (field_goals * 3)

    # Calculate the number of touchdowns
    touchdowns = touchdown_score // 7

    result = touchdowns
    return result

print(solution())