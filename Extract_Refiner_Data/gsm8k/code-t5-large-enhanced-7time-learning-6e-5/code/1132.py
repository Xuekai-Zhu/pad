def solution():
    
    # Define the number of marbles Bob will have after receiving 2 dozen more
    initial_marbles = 60

    # Define the number of marbles Bob receives in the next 2 dozen
    additional_marbles = 2 * 12

    # Calculate the total number of marbles Bob will have after receiving 2 dozen more
    total_marbles = initial_marbles + additional_marbles

    # Subtract the number of marbles Bob loses
    total_marbles -= 10

    # Display the total number of marbles Bob will have
    result = total_marbles
    return result

print(solution())