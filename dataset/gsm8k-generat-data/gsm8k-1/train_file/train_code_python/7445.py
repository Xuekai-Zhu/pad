def solution():
    """In a certain school, 2/3 of the male students like to play basketball, but only 1/5 of the female students like to play basketball. What percent of the population of the school do not like to play basketball if the ratio of the male to female students is 3:2 and there are 1000 students?"""
    total_students = 1000
    male_ratio = 3
    female_ratio = 2
    total_ratio = male_ratio + female_ratio
    male_students = total_students * (male_ratio / total_ratio)
    female_students = total_students * (female_ratio / total_ratio)
    male_bball_players = male_students * (2/3)
    female_bball_players = female_students * (1/5)
    non_bball_players = total_students - (male_bball_players + female_bball_players)
    percent_non_bball_players = (non_bball_players / total_students) * 100
    result = percent_non_bball_players
    return result

print(solution())