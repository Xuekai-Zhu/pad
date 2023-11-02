def solution():
    """Zack's number of marbles can be divided equally among three people, leaving Zack with 5. If Zack decided to give his three friends 20 marbles each and kept five, how many marbles did he initially have?"""
    # Define the number of marbles Zack has after giving 20 each to his friends
    final_marbles = 5

    # Calculate the number of marbles given to Zack's friends
    friend_marbles = 20 * 3

    # Calculate the initial number of marbles Zack had
    initial_marbles = (final_marbles + friend_marbles) * 3

    # Return the result
    result = initial_marbles
    return result

print(solution())