def solution():
    
    # Define the cost of one pair of heels and the difference in cost between the boots and the two pairs of heels
    HEEL_COST = 33
    HEEL_DIFFERENCE = 5

    # Calculate the total cost of the two pairs of heels
    total_heels_cost = 2 * HEEL_COST

    # Calculate the cost of the boots by subtracting the cost of the two pairs of heels from the total budget
    boots_cost = total_heels_cost - HEEL_DIFFERENCE

    # Display the cost of the boots
    result = boots_cost
    return result

print(solution())