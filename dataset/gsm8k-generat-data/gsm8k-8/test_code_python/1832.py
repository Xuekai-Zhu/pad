def solution():
    # Define the number of soccer balls
    soccer_balls = 20

    # Calculate the number of basketballs
    basketballs = soccer_balls + 5

    # Calculate the number of tennis balls
    tennis_balls = 2 * soccer_balls

    # Calculate the number of baseballs
    baseballs = soccer_balls + 10

    # Calculate the total number of balls
    total_balls = soccer_balls + basketballs + tennis_balls + baseballs + unknown_balls

    # Calculate the number of volleyballs
    volleyballs = 145 - total_balls

    result = volleyballs
    return result

print(solution())