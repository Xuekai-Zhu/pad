def solution():
    """Samira is the assistant coach of a soccer team playing against one of the best teams in their league. She has four dozen water bottles filled with water in a box. In the first break of the match, the 11 players on the field each take two bottles of water from Samira's box, and at the end of the game, take one more bottle each. How many bottles of water are remaining in Samira's box?"""
    bottles_per_dozen = 12
    initial_bottles = 4 * bottles_per_dozen
    bottles_taken_first_break = 11 * 2
    bottles_taken_end_game = 11 * 1
    remaining_bottles = initial_bottles - bottles_taken_first_break - bottles_taken_end_game
    result = remaining_bottles
    return result

print(solution())