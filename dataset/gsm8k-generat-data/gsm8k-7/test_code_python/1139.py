def solution():
    num_goldfish = 3
    num_platyfish = 10
    goldfish_balls = 10
    platyfish_balls = 5

    # Calculate the total number of red balls from goldfish
    total_goldfish_balls = num_goldfish * goldfish_balls

    # Calculate the total number of white balls from platyfish
    total_platyfish_balls = num_platyfish * platyfish_balls

    # Calculate the total number of balls in the fish tank
    total_balls = total_goldfish_balls + total_platyfish_balls
    result = total_balls
    return result

print(solution())