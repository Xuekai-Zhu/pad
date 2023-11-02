def solution():
    """Bertha plays tennis. Every ten games, one of her tennis balls wears out. Every five games, she loses a ball. Every four games, she buys a canister of three balls. She started with two balls and gave one to her partner. After twenty games, how many tennis balls does she have?"""
    # Initialize the number of tennis balls
    tennis_balls = 1

    # Simulate the games and track the number of tennis balls
    for i in range(1, 21):

        # Check if it's time to buy a canister of balls
        if i % 4 == 0:
            tennis_balls += 3

        # Check if a tennis ball wears out
        if i % 10 == 0:
            tennis_balls -= 1

        # Check if a tennis ball is lost
        if i % 5 == 0:
            tennis_balls -= 1

    # Add the two balls Bertha started with and gave away
    total_balls = tennis_balls + 2

    # Display the total number of tennis balls Bertha has
    result = total_balls
    return result

print(solution())