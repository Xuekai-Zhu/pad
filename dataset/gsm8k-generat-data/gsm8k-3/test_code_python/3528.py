def solution():
    """Samira is the assistant coach of a soccer team playing against one of the best teams in their league. She has four dozen water bottles filled with water in a box. In the first break of the match, the 11 players on the field each take two bottles of water from Samira's box, and at the end of the game, take one more bottle each. How many bottles of water are remaining in Samira's box?"""
    
    # Define the number of water bottles Samira has
    num_water_bottles = 4 * 12

    # Calculate the number of bottles taken during the first break
    num_bottles_first_break = 11 * 2

    # Calculate the number of bottles taken at the end of the game
    num_bottles_end_game = 11 * 1

    # Calculate the total number of bottles taken
    total_bottles_taken = num_bottles_first_break + num_bottles_end_game

    # Calculate the number of bottles remaining in the box
    bottles_remaining = num_water_bottles - total_bottles_taken

    # Display the number of bottles remaining
    result = bottles_remaining
    return result

print(solution())