def solution():
    """There are three goldfish and ten platyfish in a fish tank. Each goldfish plays with ten red balls, while each platyfish plays with five white balls. What is the total number of balls in the fish tank?"""
    # Define the number of goldfish and platyfish
    goldfish = 3
    platyfish = 10

    # Define the number of balls each type of fish plays with
    goldfish_balls = 10
    platyfish_balls = 5

    # Calculate the total number of balls in the fish tank
    total_balls = (goldfish * goldfish_balls) + (platyfish * platyfish_balls)

    # Display the total number of balls
    result = total_balls
    return result

print(solution())