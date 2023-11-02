def solution():
    """Michael has a lot of matchsticks at home and decides to use them to make miniature models. As he is about to start crafting, he has second thoughts and decides to only use half of his pile of matchsticks. He creates 30 matchsticks houses. If he has now used all of the matchsticks he intended to and each matchstick house uses 10 matchsticks, how many matchsticks did Michael have originally?"""
    num_matchstick_houses = 30
    matchsticks_per_house = 10
    total_matchsticks_used = num_matchstick_houses * matchsticks_per_house
    original_matchsticks = total_matchsticks_used * 2
    result = original_matchsticks
    return result

print(solution())