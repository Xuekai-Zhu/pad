def solution():
    """Lorenzo put three full cans of thumbtacks into his pocket and went off to work at the corkboard factory. It was Lorenzo's job, as head of quality control, to test every cork board for its ability to hold thumbtacks. He placed one thumbtack from each of the three cans of thumbtacks into every board tested. At the end of the day, he had tested 120 boards and had 30 tacks remaining in each of the three cans. What was the total combined number of thumbtacks from the three full cans?"""
    # Define the number of thumbtacks remaining in each can
    remaining_tacks = 30

    # Calculate the number of thumbtacks used in testing each board
    tacks_per_board = 3

    # Calculate the total number of thumbtacks used in testing
    total_tacks_used = tacks_per_board * 120

    # Calculate the total number of thumbtacks originally in the three cans
    total_tacks = total_tacks_used + (remaining_tacks * 3)

    # return the result
    result = total_tacks
    return result

print(solution())