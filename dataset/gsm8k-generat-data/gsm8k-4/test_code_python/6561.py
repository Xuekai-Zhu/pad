def solution():
    """Bob buys 50 feet of rope. He uses a 5th of it to make a small piece of art.
    He takes the rest and gives half of it to a friend. After that, he cuts 2-foot sections.
    How many sections does he get?"""
    # Define the total length of rope, the length used for art, and the length given to the friend
    total_length = 50
    art_length = total_length / 5
    friend_length = (total_length - art_length) / 2

    # Calculate the length of rope remaining after giving some to the friend
    remaining_length = total_length - art_length - friend_length

    # Calculate the number of 2-foot sections that can be cut from the remaining rope
    sections = remaining_length / 2

    result = int(sections)
    return result

print(solution())