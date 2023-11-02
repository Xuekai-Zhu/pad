def solution():
    """Carter is a professional drummer.  He goes through 5 sets of drum sticks per show.  After the end of each show, he tosses 6 new drum stick sets to audience members.  He does this for 30 nights straight.  How many sets of drum sticks does he go through?"""
    # Define the number of drum sticks used per show
    DRUM_STICKS_PER_SHOW = 5

    # Define the number of new drum stick sets tossed per show
    NEW_DRUM_STICK_SETS_PER_SHOW = 6

    # Define the number of nights Carter performs
    NUM_NIGHTS = 30

    # Calculate the total number of drum sticks used
    total_drum_sticks_used = DRUM_STICKS_PER_SHOW * NUM_NIGHTS

    # Calculate the total number of new drum stick sets tossed
    total_new_drum_stick_sets_tossed = NEW_DRUM_STICK_SETS_PER_SHOW * NUM_NIGHTS

    # Calculate the total number of drum sticks used, taking into account the new sets tossed
    total_drum_sticks_used_with_toss = total_drum_sticks_used + total_new_drum_stick_sets_tossed

    # Display the total number of drum sticks used
    result = total_drum_sticks_used_with_toss
    return result

print(solution())