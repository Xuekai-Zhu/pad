def solution():
    """Matthias has 40 soccer balls and 15 basketballs. 30 soccer balls and 7 basketballs have a hole in them. How many balls in total does Matthias have without holes in them?"""
    # Define the number of soccer balls and basketballs Matthias has
    soccer_balls = 40
    basketballs = 15

    # Define the number of soccer balls and basketballs with a hole in them
    soccer_holes = 30
    basketball_holes = 7

    # Calculate the number of soccer balls and basketballs without holes
    soccer_good = soccer_balls - soccer_holes
    basketballs_good = basketballs - basketball_holes

    # Calculate the total number of balls without holes
    total = soccer_good + basketballs_good

    # Display the total number of balls without holes
    result = total
    return result

print(solution())