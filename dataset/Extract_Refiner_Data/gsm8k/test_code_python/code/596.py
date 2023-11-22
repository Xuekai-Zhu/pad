def solution():
    
    # Define the initial weight and the percentage increase
    initial_weight = 8
    percentage_increase = 50

    # Calculate the new weight after the increase
    new_weight = initial_weight * (1 + percentage_increase/100)

    # Calculate the new weight after two pounds lighter
    new_weight -= 2

    # Display the new weight
    result = new_weight
    return result

print(solution())