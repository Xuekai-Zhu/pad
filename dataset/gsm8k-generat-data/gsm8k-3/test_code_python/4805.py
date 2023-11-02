def solution():
    """On the island of Castor, there are 40 chess players. A quarter of the island's chess players have never lost to an AI. How many people on the island have lost to a computer, at least once?"""
    # Calculate the number of players who have never lost to an AI
    never_lost = 40 * 0.25

    # Calculate the number of players who have lost to an AI at least once
    lost_at_least_once = 40 - never_lost

    # Display the result
    result = lost_at_least_once
    return result

print(solution())