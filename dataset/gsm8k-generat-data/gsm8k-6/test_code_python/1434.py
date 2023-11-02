def solution():
    # Calculate the total number of tennis balls used in the tournament
    first_round_balls = 8 * 5 * 3  # 8 games in the first round, each using 5 cans of tennis balls with 3 balls per can
    second_round_balls = 4 * 5 * 3  # 4 games in the second round, each using 5 cans of tennis balls with 3 balls per can
    third_round_balls = 2 * 5 * 3  # 2 games in the third round, each using 5 cans of tennis balls with 3 balls per can
    finals_balls = 1 * 5 * 3  # 1 game in the finals, using 5 cans of tennis balls with 3 balls per can
    total_balls = first_round_balls + second_round_balls + third_round_balls + finals_balls
    result = total_balls
    return result

print(solution())