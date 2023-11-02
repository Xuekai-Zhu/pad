def solution():
    """Miriam currently has 30 marbles, but she used to have more. Miriam gave her brother 60 marbles, gave her sister twice that amount and gave her friend Savanna three times the amount she currently has. How many marbles did Miriam start with?"""
    # Define the initial number of marbles
    initial_marbles = None

    # Calculate the number of marbles Miriam gave her brother
    marbles_to_brother = 60

    # Calculate the number of marbles Miriam gave her sister
    marbles_to_sister = 2 * marbles_to_brother

    # Calculate the number of marbles Miriam gave her friend
    marbles_to_friend = 3 * 30

    # Calculate the total number of marbles Miriam used to have
    total_marbles = marbles_to_brother + marbles_to_sister + marbles_to_friend + 30

    result = total_marbles
    return result

print(solution())