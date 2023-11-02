def solution():
    """20% of 50 people think horse #2 will win the big race. 60% of the remaining people think horse #7 will win. The rest of the people think horse #12 will win the big race. How many people think that horse #12 will win?"""
    total_people = 50
    horse_2_percentage = 20
    horse_7_percentage = 60
    horse_2_people = (horse_2_percentage / 100) * total_people
    remaining_people = total_people - horse_2_people
    horse_7_people = (horse_7_percentage / 100) * remaining_people
    horse_12_people = total_people - horse_2_people - horse_7_people
    result = horse_12_people
    return result

print(solution())