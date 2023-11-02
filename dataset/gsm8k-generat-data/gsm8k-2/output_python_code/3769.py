def solution():
    """Matthias has 40 soccer balls and 15 basketballs. 30 soccer balls and 7 basketballs have a hole in them. How many balls in total does Matthias have without holes in them?"""
    total_balls = 40 + 15
    hole_balls = 30 + 7
    non_hole_balls = total_balls - hole_balls
    result = non_hole_balls
    return result

print(solution())