def solution():
    """Bob buys 50 feet of rope.  He uses a 5th of it to make a small piece of art.  He takes the rest and gives half of it to the friend.  After that, he cuts 2-foot sections.  How many sections does he get?"""
    
    # Calculate the length of rope Bob has left after making a small piece of art
    rope_left = 50 - (50/5)

    # Give away half of the remaining rope to his friend
    rope_left /= 2

    # Calculate the number of 2-foot sections Bob can cut
    sections = rope_left / 2

    result = sections
    return result

print(solution())