def solution():
    """There were 600 people in the stadium when the football game started. Before the game was over, one-fourth of the boys and one-eighth of the girls left early. How many people remained to see the end of the game if there were 240 girls at the beginning of the game?"""
    total_people = 600
    girls = 240
    boys = total_people - girls
    boys_left = boys * 0.25
    girls_left = girls * 0.125
    remaining_people = total_people - boys_left - girls_left
    result = remaining_people
    return result

print(solution())