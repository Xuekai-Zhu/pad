def solution():
    
    # Define the initial number of sodas
    initial_sodas = 12

    # Calculate the number of sodas shaked up
    shaked_sodas = initial_sodas - 3

    # Calculate the number of sodas taken by Ellen's brother
    brother_sodas = 1 + 2

    # Calculate the total number of sodas taken
    total_sodas_taken = shaked_sodas + brother_sodas

    # Calculate the probability of spraying with soda
    probability = total_sodas_taken / total_sodas_taken * 100

    # Display the probability
    result = probability
    return result

print(solution())