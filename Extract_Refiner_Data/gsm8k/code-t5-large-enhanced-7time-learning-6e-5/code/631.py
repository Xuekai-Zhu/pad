def solution():
    
    # Define the total cost of Manny's classes
    total_cost = 60

    # Define the cost per class
    cost_per_class = 10

    # Calculate the total cost of the remaining classes
    remaining_cost = total_cost - cost_per_class * 10

    # Calculate the number of classes that can't sign up again
    classes_missed = remaining_cost // 10

    # Display the number of classes Manny can miss
    result = classes_missed
    return result

print(solution())