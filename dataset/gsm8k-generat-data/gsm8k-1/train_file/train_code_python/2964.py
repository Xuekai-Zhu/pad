def solution():
    """Bertha plays tennis. Every ten games, one of her tennis balls wears out. Every five games, she loses a ball. Every four games, she buys a canister of three balls. She started with two balls and gave one to her partner. After twenty games, how many tennis balls does she have?"""
    starting_balls = 2
    games_per_worn_ball = 10
    games_per_lost_ball = 5
    games_per_canister = 4
    balls_per_canister = 3
    partner_balls = 1
    games_played = 20

    # Calculate number of worn balls
    worn_balls = games_played // games_per_worn_ball

    # Calculate number of lost balls
    lost_balls = games_played // games_per_lost_ball

    # Calculate number of canisters bought
    canisters_bought = games_played // games_per_canister

    # Calculate number of balls gained from canisters
    balls_gained = canisters_bought * balls_per_canister

    # Calculate total balls at end of 20 games
    total_balls = starting_balls + balls_gained - worn_balls - lost_balls - partner_balls

    result = total_balls
    return result

print(solution())