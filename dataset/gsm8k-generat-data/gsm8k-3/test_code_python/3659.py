def solution():
    """Radhika got a new gaming system and asked everyone to get her games as gifts to add to the games she already has that she bought with her gaming system. On Christmas, she is given 12 new video games. On her birthday in February, she is given 8 more video games. Radhika already owned 1/2 the number of games as what she was given on Christmas and her birthday. How many video games does she own now?"""
    # Calculate the total number of games Radhika was given
    total_given = 12 + 8

    # Calculate the number of games Radhika owned before Christmas and her birthday
    owned_before = total_given / 2

    # Calculate Radhika's total number of games now
    total_games = owned_before + total_given

    # Display Radhika's total number of games
    result = total_games
    return result

print(solution())