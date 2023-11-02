def solution():
    """During the soccer match, The Kickers scored 2 goals in the first period and twice that amount in the second period.  The other team, The Spiders, scored half the amount that The Kickers scored in the first period and twice the amount that The Kickers scored in their second period.  What is the total amount of goals both teams scored?"""
    # Calculate the number of goals The Kickers scored in the first and second periods
    kickers_goals_1 = 2
    kickers_goals_2 = 2 * kickers_goals_1

    # Calculate the number of goals The Spiders scored in the first and second periods
    spiders_goals_1 = kickers_goals_1 / 2
    spiders_goals_2 = 2 * kickers_goals_2

    # Calculate the total number of goals scored by both teams
    total_goals = kickers_goals_1 + kickers_goals_2 + spiders_goals_1 + spiders_goals_2

    # Display the total number of goals scored
    result = total_goals
    return result

print(solution())