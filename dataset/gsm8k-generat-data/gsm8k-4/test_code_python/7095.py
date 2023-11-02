def solution():
    """There are 50 oysters on the rocks at La Push Park and 72 crabs by the beach. Eric, who loves walking by the beach, makes a note of this and goes home. The next day, he realizes only half the number of Oysters were on the rocks, and only 2/3 the number of crabs as the previous day are on the beach. How many oysters and crabs did he count in total in the two days?"""
    # Define the initial number of oysters and crabs
    initial_oysters = 50
    initial_crabs = 72

    # Calculate the number of oysters and crabs on the second day
    oysters_day2 = initial_oysters / 2
    crabs_day2 = initial_crabs * (2/3)

    # Calculate the total number of oysters and crabs counted on both days
    total_oysters = initial_oysters + oysters_day2
    total_crabs = initial_crabs + crabs_day2

    # Return the total number of oysters and crabs counted
    result = total_oysters + total_crabs
    return result

print(solution())