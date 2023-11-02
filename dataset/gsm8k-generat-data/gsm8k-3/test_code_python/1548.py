def solution():
    """Bill is trying to control the pests in his garden. Each spider he introduces eats 7 bugs, and each time he sprays the garden he reduces the total bug population to 80% of what it was previously. If the garden has 400 bugs to start, and Bill sprays once and introduces 12 spiders, how many bugs are left?"""
    # Define the initial number of bugs
    bug_population = 400

    # Spray the garden
    bug_population *= 0.8

    # Introduce the spiders
    bug_population -= 12 * 7

    # Display the number of bugs remaining
    result = bug_population
    return result

print(solution())