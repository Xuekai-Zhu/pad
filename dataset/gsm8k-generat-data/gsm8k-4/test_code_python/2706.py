def solution():
    """A leaf is being blown down a sidewalk by swirling gusts of wind. For every five feet that a gust blows it forward, the wind swirls and blows it back two feet. How many feet has it traveled down the sidewalk after 11 gusts of wind?"""
    # Define the initial position of the leaf
    position = 0

    # Define the number of gusts
    num_gusts = 11

    # Calculate the position of the leaf after each gust
    for i in range(num_gusts):
        # Each gust moves the leaf forward by 5 feet
        position += 5
        
        # Every sixth gust blows the leaf back by 2 feet
        if (i+1) % 6 == 0:
            position -= 2

    # Return the final position of the leaf
    result = position
    return result

print(solution())