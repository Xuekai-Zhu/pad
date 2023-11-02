def solution():
    """There were 600 people in the stadium when the football game started. Before the game was over, one-fourth of the boys and one-eighth of the girls left early. How many people remained to see the end of the game if there were 240 girls at the beginning of the game?"""
    num_people_start = 600
    num_girls_start = 240
    num_boys_start = num_people_start - num_girls_start
    num_boys_left = num_boys_start / 4
    num_girls_left = num_girls_start / 8
    num_people_left = num_boys_left + num_girls_left
    num_people_end = num_people_start - num_people_left
    result = num_people_end
    return result

print(solution())