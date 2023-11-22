def solution():
    
    # Define the percentage of water used for industrial purposes
    industrial_percentage = 80

    # Calculate the total percentage of water used for industrial purposes
    industrial_percentage_total = industrial_percentage / 100

    # Calculate the total percentage of water used for non-industrial purposes
    non_industrial_percentage_total = (100 - industrial_percentage_total) / 100

    # Display the percentage of water used for non-industrial purposes
    result = non_industrial_percentage_total
    return result

print(solution())