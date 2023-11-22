def solution():
    
    # Define the initial number of marbles
    initial_marbles = 30

    # Calculate the number of marbles given to Jamie
    jamie_marbles = initial_marbles / 5

    # Calculate the number of marbles left after giving some to Jamie
    remaining_marbles = initial_marbles - jamie_marbles

    # Calculate the number of marbles given to Donald
    donald_marbles = 10

    # Calculate the final number of marbles left for Dean
    final_marbles = remaining_marbles - donald_marbles

    # Display the final number of marbles left for Dean
    result = final_marbles
    return result

print(solution())