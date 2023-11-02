def solution():
    """Melissa bought 4 packs of tennis balls for $24 in total. Each pack contains 3 balls per pack. How much did it cost Melissa for each tennis ball?"""
    # Define the number of packs of tennis balls and the total cost
    num_packs = 4
    total_cost = 24

    # Define the number of tennis balls per pack
    num_balls_per_pack = 3

    # Calculate the total number of tennis balls
    total_balls = num_packs * num_balls_per_pack

    # Calculate the cost per tennis ball
    cost_per_ball = total_cost / total_balls

    # Round the answer to 2 decimal places
    result = round(cost_per_ball, 2)
    return result

print(solution())