def solution():
    """Bertha plays tennis. Every ten games, one of her tennis balls wears out. Every five games, she loses a ball. Every four games, she buys a canister of three balls. She started with two balls and gave one to her partner. After twenty games, how many tennis balls does she have?"""
    # Define the initial number of tennis balls
    tennis_balls = 1

    # Play 20 games
    for i in range(20):
        # Check if a tennis ball has worn out
        if (i + 1) % 10 == 0:
            tennis_balls -= 1
        # Check if a tennis ball has been lost
        if (i + 1) % 5 == 0:
            tennis_balls -= 1
        # Check if a new canister of balls has been bought
        if (i + 1) % 4 == 0:
            tennis_balls += 3

    # Add the initial number of tennis balls
    tennis_balls += 1

    # Display the final number of tennis balls
    result = tennis_balls
    return result

print(solution())