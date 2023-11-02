def solution():
    
    # Define the ratio of men to women on the bus
    men_to_women_ratio = 5/9

    # Calculate the total number of passengers on the bus
    total_passengers = 84

    # Calculate the number of men and women on the bus
    men = total_passengers * men_to_women_ratio
    women = total_passengers - 20

    # Calculate the number of women remaining on the bus
    women_remaining = women - men

    # Display the number of women remaining on the bus
    result = women_remaining
    return result

print(solution())