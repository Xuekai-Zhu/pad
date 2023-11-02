def solution():
    """Lorenzo put three full cans of thumbtacks into his pocket and went off to work at the corkboard factory. It was Lorenzo's job, as head of quality control, to test every cork board for its ability to hold thumbtacks. He placed one thumbtack from each of the three cans of thumbtacks into every board tested. At the end of the day, he had tested 120 boards and had 30 tacks remaining in each of the three cans. What was the total combined number of thumbtacks from the three full cans?"""
    boards_tested = 120
    tacks_remaining = 30
    tacks_per_board = 3
    total_tacks_tested = boards_tested * tacks_per_board
    total_tacks_used = total_tacks_tested - (tacks_remaining * 3)
    result = total_tacks_used
    return result

print(solution())