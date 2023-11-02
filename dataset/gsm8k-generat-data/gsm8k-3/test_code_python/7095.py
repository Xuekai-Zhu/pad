def solution():
    """There are 50 oysters on the rocks at La Push Park and 72 crabs by the beach. Eric, who loves walking by the beach, makes a note of this and goes home.
    The next day, he realizes only half the number of Oysters were on the rocks, and only 2/3 the number of crabs as the previous day are on the beach.
    How many oysters and crabs did he count in total in the two days?"""
    
    # Define the initial number of oysters and crabs
    initial_oysters = 50
    initial_crabs = 72

    # Calculate the number of oysters and crabs on the second day
    final_oysters = initial_oysters / 2
    final_crabs = initial_crabs * 2 / 3

    # Calculate the total number of oysters and crabs counted in both days
    total_oysters = initial_oysters + final_oysters
    total_crabs = initial_crabs + final_crabs

    # Display the total number of oysters and crabs
    result = total_oysters + total_crabs
    return result

print(solution())