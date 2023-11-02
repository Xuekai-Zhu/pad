def solution():
    """Bill is trying to control the pests in his garden. Each spider he introduces eats 7 bugs, and each time he sprays the garden he reduces the total bug population to 80% of what it was previously. If the garden has 400 bugs to start, and Bill sprays once and introduces 12 spiders, how many bugs are left?"""
    # Define the starting bug population
    bugs = 400

    # Apply the spray to the bug population
    bugs = bugs * 0.8

    # Introduce the spiders to the garden
    bugs -= 12 * 7

    # Return the final bug population
    result = bugs
    return result

print(solution())