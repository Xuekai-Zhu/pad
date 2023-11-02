def solution():
    """Reynald is the head of the varsity department, and he bought 145 balls. Twenty were soccer balls. There were five more basketballs than the soccer balls. Twice the number of soccer balls were tennis balls. There were ten more baseballs than the soccer balls, and the rest were volleyballs. How many were volleyballs?"""
    # Define the number of soccer balls
    soccer_balls = 20

    # Calculate the number of basketballs
    basketballs = soccer_balls + 5

    # Calculate the number of tennis balls
    tennis_balls = 2 * soccer_balls

    # Calculate the number of baseballs
    baseballs = soccer_balls + 10

    # Calculate the number of volleyballs
    volleyballs = 145 - (soccer_balls + basketballs + tennis_balls + baseballs)

    # Display the number of volleyballs
    result = volleyballs
    return result

print(solution())