def solution():
    # Calculate the number of tennis balls left after 20 games
    initial_balls = 2
    worn_out_balls = 20 // 10  # every ten games, one ball wears out
    lost_balls = 20 // 5  # every five games, one ball is lost
    bought_canisters = 20 // 4  # every four games, a canister of three balls is bought
    bought_balls = bought_canisters * 3
    total_balls = initial_balls - 1 - lost_balls + bought_balls - worn_out_balls  # Bertha gave one ball to her partner
    result = total_balls
    return result

print(solution())