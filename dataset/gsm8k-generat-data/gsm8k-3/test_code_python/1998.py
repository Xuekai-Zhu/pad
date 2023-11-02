def solution():
    """Harold had 100 marbles. He kept 20 marbles and shared the rest evenly among his 5 friends. How many marbles did each friend get?"""
    # Define the total number of marbles and the number Harold kept
    total_marbles = 100
    harold_kept = 20

    # Calculate the number of marbles to be shared
    shared_marbles = total_marbles - harold_kept

    # Divide the shared marbles evenly among Harold's 5 friends
    marbles_per_friend = shared_marbles / 5

    # Display the number of marbles each friend received
    result = marbles_per_friend
    return result

print(solution())