def solution():
    """Of the 100 soccer balls that Nova went to inflate, 40 percent had holes in them and could not inflate, while 20% of the remaining balls were overinflated and exploded. How many balls were inflated successfully and could be used?"""
    total_balls = 100
    defective_balls = int(total_balls * 0.4)
    useable_balls = total_balls - defective_balls
    exploded_balls = int(useable_balls * 0.2)
    inflated_balls = useable_balls - exploded_balls
    result = inflated_balls
    return result

print(solution())