def solution():
    """Michael has a lot of matchsticks at home and decides to use them to make miniature models. As he is about to start crafting, he has second thoughts and decides to only use half of his pile of matchsticks. He creates 30 matchsticks houses. If he has now used all of the matchsticks he intended to and each matchstick house uses 10 matchsticks, how many matchsticks did Michael have originally?"""
    # Define the number of matchstick houses created and the number of matchsticks used per house
    HOUSES_CREATED = 30
    MATCHSTICKS_PER_HOUSE = 10

    # Calculate the total number of matchsticks used
    total_matchsticks_used = HOUSES_CREATED * MATCHSTICKS_PER_HOUSE

    # Calculate the original number of matchsticks using the fact that Michael only used half of them
    original_matchsticks = total_matchsticks_used * 2

    # Display the original number of matchsticks
    result = original_matchsticks
    return result

print(solution())