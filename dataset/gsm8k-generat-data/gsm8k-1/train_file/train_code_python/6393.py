def solution():
    """Of the 100 soccer balls that Nova went to inflate, 40 percent had holes in them and could not inflate, while 20% of the remaining balls were overinflated and exploded. How many balls were inflated successfully and could be used?"""
    total_balls = 100
    hole_percent = 40
    overinflated_percent = 20
    inflated_balls = total_balls * (100 - hole_percent) / 100
    usable_balls = inflated_balls * (100 - overinflated_percent) / 100
    result = usable_balls
    return result

print(solution())