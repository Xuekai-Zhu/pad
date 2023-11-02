def solution():
    # Calculate Tom's goals on the first day
    tom_first_day = 2 + 3  # Gina scored 3 less than Tom

    # Calculate Gina's goals on the second day
    gina_second_day = 6 - 2  # Gina scored 2 less than Tom

    # Calculate the total goals scored by Gina and Tom
    total_goals = 2 + tom_first_day + gina_second_day + 6  # Gina scored 2 goals on the first day, and Tom scored 6 goals on the second day

    result = total_goals
    return result

print(solution())