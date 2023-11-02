def solution():
    
    # Define the initial number of marbles
    initial_marbles = 10

    # Calculate the number of marbles Brendan dropped
    dropped_marbles = initial_marbles // 2

    # Calculate the number of marbles Brendan picked up with
    picked_up_marbles = 3

    # Calculate the number of marbles Brendan ended up with
    end_up_marbles = initial_marbles - dropped_marbles - picked_up_marbles

    # Display the number of marbles Brendan ended up with
    result = end_up_marbles
    return result

print(solution())