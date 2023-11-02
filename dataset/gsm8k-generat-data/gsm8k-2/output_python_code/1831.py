def solution():
    """Reynald is the head of the varsity department, and he bought 145 balls. Twenty were soccer balls. There were five more basketballs than the soccer balls. Twice the number of soccer balls were tennis balls. There were ten more baseballs than the soccer balls, and the rest were volleyballs. How many were volleyballs?"""
    total_balls = 145
    soccer_balls = 20
    basketballs = soccer_balls + 5
    tennis_balls = 2 * soccer_balls
    baseballs = soccer_balls + 10
    total_known_balls = soccer_balls + basketballs + tennis_balls + baseballs
    volleyballs = total_balls - total_known_balls
    result = volleyballs
    return result

print(solution())