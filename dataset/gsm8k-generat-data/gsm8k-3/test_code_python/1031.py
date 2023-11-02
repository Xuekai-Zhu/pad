def solution():
    """There were 600 people in the stadium when the football game started. Before the game was over, one-fourth of the boys and one-eighth of the girls left early. How many people remained to see the end of the game if there were 240 girls at the beginning of the game?"""
    # Define the number of girls and boys at the beginning of the game
    girls = 240
    boys = 600 - girls

    # Calculate the number of people who left early
    boys_left = boys // 4
    girls_left = girls // 8
    total_left = boys_left + girls_left

    # Calculate the number of people who remained
    remained = 600 - total_left

    # Display the number of people who remained
    result = remained
    return result

print(solution())