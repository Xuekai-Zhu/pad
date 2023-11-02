def solution():
    """Carter is a professional drummer. He goes through 5 sets of drum sticks per show. After the end of each show, he tosses 6 new drum stick sets to audience members. He does this for 30 nights straight. How many sets of drum sticks does he go through?"""
    # Define the number of drum sticks used per show and given away
    DRUM_STICKS_PER_SHOW = 5
    NEW_DRUM_STICKS_PER_SHOW = 6

    # Define the number of shows played
    SHOWS_PLAYED = 30

    # Calculate the total number of drum sticks used, including those given away
    total_drum_sticks = DRUM_STICKS_PER_SHOW * SHOWS_PLAYED + NEW_DRUM_STICKS_PER_SHOW * SHOWS_PLAYED

    # return the result
    result = total_drum_sticks
    return result

print(solution())