def solution():
    """Zack's number of marbles can be divided equally among three people, leaving Zack with 5. If Zack decided to give his three friends 20 marbles each and kept five, how many marbles did he initially have?"""
    # Define the number of marbles Zack kept after giving his friends 20 each
    marbles_left = 5

    # Calculate the total number of marbles Zack gave his friends
    marbles_given = 3 * 20

    # Calculate the total number of marbles Zack initially had
    total_marbles = marbles_left + marbles_given

    # Find the initial number of marbles that can be divided equally among three people
    initial_marbles = total_marbles - marbles_left
    while(initial_marbles % 3 != 0):
        initial_marbles += 1

    # Return the initial number of marbles
    result = initial_marbles
    return result

print(solution())