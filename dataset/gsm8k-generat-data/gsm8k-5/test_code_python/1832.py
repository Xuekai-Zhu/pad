def solution():
    total_balls = 145  # Reynald bought 145 balls in total
    soccer_balls = 20  # Among them, 20 were soccer balls
    basketballs = soccer_balls + 5  # There were 5 more basketballs than soccer balls
    tennis_balls = 2 * soccer_balls  # Twice the number of soccer balls were tennis balls
    baseballs = soccer_balls + 10  # There were 10 more baseballs than soccer balls

    # Calculate the number of volleyballs
    volleyballs = total_balls - soccer_balls - basketballs - tennis_balls - baseballs
    result = volleyballs
    return result

print(solution())