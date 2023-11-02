def solution():
    # Calculate the number of tomatoes Haruto has left after birds ate some and he gave half to his friend
    initial_tomatoes = 127
    eaten_tomatoes = 19
    remaining_tomatoes = initial_tomatoes - eaten_tomatoes
    remaining_tomatoes = remaining_tomatoes / 2  # Haruto gave half of his tomatoes to his friend
    result = remaining_tomatoes
    return result

print(solution())