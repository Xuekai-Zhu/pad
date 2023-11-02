def solution():
    """Leticia, Nina, and Rosalie have a total of 25 people on their dance team. If 8 people quit, but 13 new people got in, how many people are there now on the team?"""
    # Define the initial number of people on the team
    initial_people = 25

    # Subtract the number of people who quit
    after_quitters = initial_people - 8

    # Add the number of new people who joined
    after_newbies = after_quitters + 13

    # return the result
    result = after_newbies
    return result

print(solution())