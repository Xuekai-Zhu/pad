def solution():
    
    # Define the number of brownies needed
    brownies_needed = 12

    # Calculate the number of brownies sent to the party
    brownies_from_party = 0.5 * 12

    # Calculate the number of brownies waiting for the party
    brownies_waiting = 4 * 12

    # Calculate the number of brownies eaten during the party
    brownies_eaten = 0.5 * 12

    # Calculate the total number of brownies
    total_brownies = brownies_from_party + brownies_from_party - brownies_eaten

    # Display the total number of brownies left over
    result = total_brownies
    return result

print(solution())