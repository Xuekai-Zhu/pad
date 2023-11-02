def solution():
    """Lorenzo put three full cans of thumbtacks into his pocket and went off to work at the corkboard factory.
    It was Lorenzo's job, as head of quality control, to test every cork board for its ability to hold thumbtacks.
    He placed one thumbtack from each of the three cans of thumbtacks into every board tested. 
    At the end of the day, he had tested 120 boards and had 30 tacks remaining in each of the three cans. 
    What was the total combined number of thumbtacks from the three full cans?"""
    # Let x be the number of thumbtacks in each can
    # After placing 1 thumbtack from each can in a board, each can has x-1 thumbtacks left
    # After testing 120 boards, there are 3 * (x-1) + 30 thumbtacks left
    # We also know that 3x - 90 = 120 (the original number of thumbtacks minus the number left at the end of the day)
    # Solving for x, we get x = 70
    # So the total combined number of thumbtacks is 3 * 70 = 210

    result = 210
    return result

print(solution())