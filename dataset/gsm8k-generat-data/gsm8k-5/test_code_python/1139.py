def solution():
    # Calculate the total number of red balls (for goldfish) in the tank
    goldfish_balls = 3 * 10  # Three goldfish, each playing with 10 red balls

    # Calculate the total number of white balls (for platyfish) in the tank
    platyfish_balls = 10 * 5  # Ten platyfish, each playing with 5 white balls

    # Calculate the total number of balls in the fish tank
    total_balls = goldfish_balls + platyfish_balls
    result = total_balls
    return result

print(solution())