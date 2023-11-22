def solution():
    
    # Define the number of goals scored by Richie
    richie_goals = 80

    # Calculate the number of goals scored by Mark
    mark_goals = richie_goals - 20

    # Calculate the number of goals scored by Anna
    anna_goals = richie_goals - 45

    # Calculate the total number of goals scored by all three teenagers
    total_goals = richie_goals + mark_goals + anna_goals

    # Display the total number of goals scored
    result = total_goals
    return result

print(solution())