def solution():
    
    # Define the number of marbles bought from Johanna and the store
    johanna_marbles = 20
    store_marbles = 50

    # Calculate the number of marbles given to his father
    father_marbles = johanna_marbles * (2/5)

    # Calculate the total number of marbles
    total_marbles = johanna_marbles + store_marbles + father_marbles

    # Calculate the total weight of the marbles
    total_weight = total_marbles * 2

    # Display the total weight
    result = total_weight
    return result

print(solution())