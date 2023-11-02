def solution():
    """There are three goldfish and ten platyfish in a fish tank. Each goldfish plays with ten red balls, while each platyfish plays with five white balls. What is the total number of balls in the fish tank?"""
    goldfish_count = 3
    platyfish_count = 10
    goldfish_balls = 10
    platyfish_balls = 5
    total_balls = (goldfish_count * goldfish_balls) + (platyfish_count * platyfish_balls)
    result = total_balls
    return result

print(solution())