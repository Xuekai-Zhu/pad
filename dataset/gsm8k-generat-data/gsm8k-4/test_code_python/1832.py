def solution():
    """Reynald is the head of the varsity department, and he bought 145 balls. Twenty were soccer balls. There were five more basketballs than the soccer balls. Twice the number of soccer balls were tennis balls. There were ten more baseballs than the soccer balls, and the rest were volleyballs. How many were volleyballs?"""
    # Define the number of soccer balls
    soccer_balls = 20

    # Define the number of basketballs (5 more than soccer balls)
    basketballs = soccer_balls + 5

    # Define the number of tennis balls (twice the number of soccer balls)
    tennis_balls = soccer_balls * 2

    # Define the number of baseballs (10 more than soccer balls)
    baseballs = soccer_balls + 10

    # Calculate the number of all the other balls
    other_balls = soccer_balls + basketballs + tennis_balls + baseballs

    # Calculate the number of volleyballs
    volleyballs = 145 - other_balls

    # return the result
    result = volleyballs
    return result

print(solution())