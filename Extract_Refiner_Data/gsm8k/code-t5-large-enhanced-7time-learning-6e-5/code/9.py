def solution():
    
    # Define the number of vacuum cleaners left
    vacuum_cleaners_left = 5

    # Calculate the number of vacuum cleaners sold at the green house
    green_house_cleaners = vacuum_cleaners_left / 3

    # Calculate the number of vacuum cleaners sold to the red house
    red_house_cleaners = green_house_cleaners + 2

    # Calculate the number of vacuum cleaners left at the orange house
    orange_house_cleaners = vacuum_cleaners_left / 2

    # Calculate the total number of vacuum cleaners sold
    total_cleaners_sold = green_house_cleaners + red_house_cleaners + orange_house_cleaners

    # Calculate the number of vacuum cleaners Melanie started with
    starting_cleaners = total_cleaners_sold

    # Display the number of vacuum cleaners Melanie started with
    result = starting_cleaners
    return result

print(solution())