def solution():
    """Gina and Tom were playing football. On the first day, Gina scored two goals, which was three less than Tom. On the second day, Gina scored two goals less than Tom who scored six goals. How many goals did Gina and Tom score during these two days?"""
    # Calculate Tom's goals on the first day
    tom_day1 = 2 + 3

    # Calculate Gina's goals on the second day
    gina_day2 = 6 - 2

    # Calculate the total number of goals scored by Gina and Tom
    total_goals = tom_day1 + gina_day2

    # Display the total number of goals
    result = total_goals
    return result

print(solution())