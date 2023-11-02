def solution():
    total_people = 600  # There were 600 people in the stadium at the beginning of the game
    girls = 240  # There were 240 girls in the stadium at the beginning of the game

    # Calculate how many boys were in the stadium at the beginning of the game
    boys = total_people - girls

    # Calculate how many boys left early
    boys_left = boys / 4

    # Calculate how many girls left early
    girls_left = girls / 8

    # Calculate how many people remained to see the end of the game
    people_remaining = total_people - boys_left - girls_left
    result = people_remaining
    return result

print(solution())