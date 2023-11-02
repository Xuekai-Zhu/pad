def solution():
    """Samira is the assistant coach of a soccer team playing against one of the best teams in their league. She has four dozen water bottles filled with water in a box. In the first break of the match, the 11 players on the field each take two bottles of water from Samira's box, and at the end of the game, take one more bottle each. How many bottles of water are remaining in Samira's box?"""
    # Define the number of water bottles in Samira's box
    num_bottles = 4 * 12

    # Calculate the number of bottles taken during the break
    num_bottles_first_break = 11 * 2

    # Calculate the number of bottles taken at the end of the game
    num_bottles_end_game = 11 * 1

    # Calculate the total number of bottles taken
    num_bottles_taken = num_bottles_first_break + num_bottles_end_game

    # Calculate the number of bottles remaining
    num_bottles_remaining = num_bottles - num_bottles_taken

    # return the result
    result = num_bottles_remaining
    return result

print(solution())