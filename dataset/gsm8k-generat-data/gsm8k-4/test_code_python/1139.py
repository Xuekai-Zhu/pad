def solution():
    """There are three goldfish and ten platyfish in a fish tank. Each goldfish plays with ten red balls, while each platyfish plays with five white balls. What is the total number of balls in the fish tank?"""
    # Define the number of goldfish, the number of platyfish, and the number of balls they play with
    goldfish_count = 3
    platyfish_count = 10
    goldfish_balls = 10
    platyfish_balls = 5

    # Calculate the total number of red balls played with by the goldfish
    total_goldfish_balls = goldfish_count * goldfish_balls

    # Calculate the total number of white balls played with by the platyfish
    total_platyfish_balls = platyfish_count * platyfish_balls

    # Calculate the total number of balls in the fish tank
    total_balls = total_goldfish_balls + total_platyfish_balls

    # return the result
    result = total_balls
    return result

print(solution())