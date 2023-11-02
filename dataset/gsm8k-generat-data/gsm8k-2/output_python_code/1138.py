def solution():
    """There are three goldfish and ten platyfish in a fish tank. Each goldfish plays with ten red balls, while each platyfish plays with five white balls. What is the total number of balls in the fish tank?"""
    goldfish = 3
    platyfish = 10
    goldfish_balls = 10 * goldfish
    platyfish_balls = 5 * platyfish
    total_balls = goldfish_balls + platyfish_balls
    result = total_balls
    return result

print(solution())