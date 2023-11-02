def solution():
    current_marbles = 30  # Miriam currently has 30 marbles
    brother_marbles = 60  # Miriam gave her brother 60 marbles
    sister_marbles = 2 * brother_marbles  # Miriam gave her sister twice the amount she gave her brother
    friend_marbles = 3 * current_marbles  # Miriam gave her friend Savanna three times the amount she currently has

    # Calculate the total number of marbles Miriam had initially
    initial_marbles = current_marbles + brother_marbles + sister_marbles + friend_marbles
    result = initial_marbles
    return result

print(solution())