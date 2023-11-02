def solution():
    # Calculate the number of tennis balls used in each round
    first_round_balls = 8 * 5 * 3
    second_round_balls = 4 * 5 * 3
    third_round_balls = 2 * 5 * 3
    finals_balls = 1 * 5 * 3

    # Calculate the total number of tennis balls used in the tournament
    total_balls = first_round_balls + second_round_balls + third_round_balls + finals_balls
    result = total_balls
    return result

print(solution())