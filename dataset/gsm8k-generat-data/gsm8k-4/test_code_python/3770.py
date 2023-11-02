def solution():
    """Matthias has 40 soccer balls and 15 basketballs. 30 soccer balls and 7 basketballs have a hole in them. How many balls in total does Matthias have without holes in them?"""
    # Define the initial number of soccer balls and basketballs
    soccer_balls = 40
    basketballs = 15

    # Define the number of soccer balls and basketballs with a hole in them
    soccer_holes = 30
    basketball_holes = 7

    # Calculate the number of soccer balls and basketballs without holes
    soccer_no_holes = soccer_balls - soccer_holes
    basketballs_no_holes = basketballs - basketball_holes

    # Calculate the total number of balls without holes
    total_no_holes = soccer_no_holes + basketballs_no_holes

    # return the result
    result = total_no_holes
    return result

print(solution())