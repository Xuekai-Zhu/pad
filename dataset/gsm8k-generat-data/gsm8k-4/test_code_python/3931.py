def solution():
    """Gina and Tom were playing football. On the first day, Gina scored two goals, which was three less than Tom. On the second day, Gina scored two goals less than Tom who scored six goals. How many goals did Gina and Tom score during these two days?"""
    # Calculate Tom's goals on the first day
    tom_first_day = 2 + 3

    # Calculate Gina's goals on the second day
    gina_second_day = 6 - 2

    # Calculate the total number of goals scored by both on both days
    total_goals = tom_first_day + gina_second_day

    # Define the result as a tuple of Gina and Tom's goals
    result = (tom_first_day, total_goals - tom_first_day)

    return result

print(solution())