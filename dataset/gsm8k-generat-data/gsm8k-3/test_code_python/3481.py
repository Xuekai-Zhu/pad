def solution():
    """Miriam currently has 30 marbles, but she used to have more. Miriam gave her brother 60 marbles, gave her sister twice that amount and gave her friend Savanna three times the amount she currently has. How many marbles did Miriam start with?"""
    # Define the number of marbles currently owned by Miriam
    current_marbles = 30

    # Calculate the number of marbles given to Miriam's brother
    brother_marbles = 60

    # Calculate the number of marbles given to Miriam's sister
    sister_marbles = brother_marbles * 2

    # Calculate the number of marbles given to Savanna
    savanna_marbles = current_marbles * 3

    # Calculate the total number of marbles Miriam used to have
    total_marbles = current_marbles + brother_marbles + sister_marbles + savanna_marbles

    # Display the total number of marbles Miriam used to have
    result = total_marbles
    return result

print(solution())