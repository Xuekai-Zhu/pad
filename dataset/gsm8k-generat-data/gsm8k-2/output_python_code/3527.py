def solution():
    """Samira is the assistant coach of a soccer team playing against one of the best teams in their league. She has four dozen water bottles filled with water in a box. In the first break of the match, the 11 players on the field each take two bottles of water from Samira's box, and at the end of the game, take one more bottle each. How many bottles of water are remaining in Samira's box?"""
    total_bottles = 4 * 12
    players = 11
    first_break_bottles = players * 2
    end_game_bottles = players
    remaining_bottles = total_bottles - first_break_bottles - end_game_bottles
    result = remaining_bottles
    return result

print(solution())