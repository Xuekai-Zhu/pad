def solution():
    """Carolyn buys a silverware set with 6 knives, 12 forks, and three times as many spoons as knives. Then her friend trades her 10 knives for 6 spoons. What percentage of Carolyn's silverware is knives?"""
    # Define the initial number of knives, forks, and spoons
    knives = 6
    forks = 12
    spoons = 3*knives

    # Trade 10 knives for 6 spoons
    knives -= 10
    spoons += 6

    # Calculate the total number of pieces of silverware
    total = knives + forks + spoons

    # Calculate the percentage of silverware that is knives
    knife_percentage = (knives / total) * 100

    # return the result
    result = knife_percentage
    return result

print(solution())