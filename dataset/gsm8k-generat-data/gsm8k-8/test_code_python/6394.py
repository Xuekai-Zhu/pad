def solution():
    # Define the total number of balls and calculate the number that were defective
    total_balls = 100
    defective_balls = int(total_balls * 0.4)

    # Calculate the number of remaining balls and the number that exploded
    remaining_balls = total_balls - defective_balls
    exploded_balls = int(remaining_balls * 0.2)

    # Calculate the number of inflated and usable balls
    inflated_balls = remaining_balls - exploded_balls
    result = inflated_balls
    return result

print(solution())