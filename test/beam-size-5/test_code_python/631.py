def solution():
    
    # Define the cost per class and the number of classes
    COST_PER_CLASS = 10
    NUM_CLASSES = 10

    # Calculate the total cost of the classes
    total_cost = COST_PER_CLASS * NUM_CLASSES

    # Calculate the cost of the remaining classes
    remaining_cost = 60 - total_cost

    # Calculate the number of classes Manny can miss before they won't sign him up again
    num_missed_classes = remaining_cost // COST_PER_CLASS

    # Display the number of classes Manny can miss before they won't sign him up again
    result = num_missed_classes
    return result

print(solution())