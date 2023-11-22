def solution():
    
    # Define the total number of marbles
    total_marbles = 52

    # Calculate the number of marbles given to Dallas after dropping 4
    dallas_marbles = 21 - 4

    # Calculate the number of marbles given to Darla
    darla_marbles = total_marbles - dallas_marbles

    # Display the number of marbles given to Darla
    result = darla_marbles
    return result

print(solution())