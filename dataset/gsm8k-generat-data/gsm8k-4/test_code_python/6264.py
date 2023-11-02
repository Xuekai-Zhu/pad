def solution():
    """There were 133 people at a camp. There were 33 more boys than girls. How many girls were at the camp?"""
    # Define the total number of people and the difference in number between boys and girls
    total_people = 133
    boys_girls_difference = 33

    # Set up the equations for the number of boys and girls
    # Let x be the number of girls
    # Then x + boys_girls_difference = the number of boys
    # And x + (x + boys_girls_difference) = total_people
    # Simplifying these equations, we get:
    # 2x + boys_girls_difference = total_people
    # Solving for x, we get:
    # x = (total_people - boys_girls_difference) / 2

    # Calculate the number of girls
    girls = (total_people - boys_girls_difference) / 2

    result = girls
    return result

print(solution())