def solution():
    
    # Define the ratio of men to women
    MEN_TO_WOMEN_RATIO = 5/9

    # Calculate the total number of passengers on the bus
    total_passengers = 84

    # Calculate the number of men on the bus
    men = MEN_TO_WOMEN_RATIO * total_passengers

    # Calculate the number of women on the bus
    women = total_passengers - men

    # Calculate the number of women remaining on the bus
    women_remaining = women - 20

    # Display the number of women remaining on the bus
    result = women_remaining
    return result

print(solution())