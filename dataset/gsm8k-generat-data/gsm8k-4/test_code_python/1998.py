def solution():
    """Harold had 100 marbles. He kept 20 marbles and shared the rest evenly among his 5 friends. How many marbles did each friend get?"""
    # Define the initial number of marbles
    initial_marbles = 100

    # Define the number of marbles Harold kept
    harold_marbles = 20

    # Calculate the number of marbles to be shared among the friends
    shared_marbles = initial_marbles - harold_marbles

    # Calculate the number of marbles each friend gets
    friend_marbles = shared_marbles / 5

    # Return the result
    result = friend_marbles
    return result

print(solution())