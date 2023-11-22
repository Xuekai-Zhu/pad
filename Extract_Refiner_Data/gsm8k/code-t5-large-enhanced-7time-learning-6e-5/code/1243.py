def solution():
    
    # Define the initial number of marbles
    initial_marbles = 10

    # Calculate the number of marbles after tripping over the pebble
    dropped_marbles = initial_marbles / 2

    # Calculate the number of marbles after scrambled to search
    scrambled_marbles = dropped_marbles + 3

    # Calculate the number of marbles after inspected
    inspected_marbles = initial_marbles - scrambled_marbles

    # Calculate the number of marbles Brendan has left
    remaining_marbles = inspected_marbles

    # Display the number of marbles Brendan has left
    result = remaining_marbles
    return result

print(solution())