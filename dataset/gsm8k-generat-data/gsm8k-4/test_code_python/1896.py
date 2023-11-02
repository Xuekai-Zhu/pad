def solution():
    """Yesterday, Bruce and Michael were playing football in the park. Bruce scored 4 goals While Michael scored 3 times more than Bruce. How many goals did Bruce and Michael both score?"""
    # Bruce scored 4 goals
    bruce_goals = 4

    # Michael scored 3 times more than Bruce
    michael_goals = 3 * bruce_goals

    # Calculate the total number of goals
    total_goals = bruce_goals + michael_goals

    # Return the result
    result = total_goals
    return result

print(solution())