def solution():
    
    # Define the initial number of marbles
    initial_marbles = 30

    # Calculate the number of marbles given to Jamie
    jamie_marbles = initial_marbles // 5

    # Calculate the number of marbles given to Donald
    donald_marbles = initial_marbles - jamie_marbles - 10

    # Calculate the number of marbles left for Dean
    dean_marbles = initial_marbles - jamie_marbles - donald_marbles

    # Display the number of marbles left for Dean
    result = dean_marbles
    return result

print(solution())