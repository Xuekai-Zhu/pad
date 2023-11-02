def solution():
    """There were 600 people in the stadium when the football game started. Before the game was over, one-fourth of the boys and one-eighth of the girls left early. How many people remained to see the end of the game if there were 240 girls at the beginning of the game?"""
    # Define the initial number of people and number of girls
    initial_people = 600
    initial_girls = 240

    # Calculate the number of boys
    initial_boys = initial_people - initial_girls

    # Calculate the number of people who left early
    boys_left = initial_boys / 4
    girls_left = initial_girls / 8

    # Calculate the number of people remaining
    remaining_people = initial_people - boys_left - girls_left

    # Return the result
    result = remaining_people
    return result

print(solution())