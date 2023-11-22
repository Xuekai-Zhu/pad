def solution():
    
    # Define the initial number of marbles
    initial_marbles = 52

    # Define the number of marbles Paul's friend gave him
    friend_marbles = 28

    # Calculate the number of marbles Paul has left
    remaining_marbles = initial_marbles - friend_marbles

    # Calculate the number of marbles Paul lost
    lost_marbles = remaining_marbles / 4

    # Calculate the number of marbles Paul has left
    final_marbles = remaining_marbles - lost_marbles

    # Display the final number of marbles Paul has left
    result = final_marbles
    return result

print(solution())