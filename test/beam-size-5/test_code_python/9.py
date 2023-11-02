def solution():
    
    # Define the initial number of vacuum cleaners
    vacuum_cleaners = 5

    # Calculate the number of vacuum cleaners sold at the green house
    green_cleaners = vacuum_cleaners // 3

    # Calculate the number of vacuum cleaners remaining after the green house
    remaining_cleaners = vacuum_cleaners - green_cleaners

    # Calculate the number of vacuum cleaners sold at the red house
    red_cleaners = remaining_cleaners // 2

    # Calculate the number of vacuum cleaners remaining after the red house
    remaining_cleaners = remaining_cleaners - red_cleaners

    # Calculate the number of vacuum cleaners at the orange house
    orange_cleaners = remaining_cleaners // 2

    # Calculate the number of vacuum cleaners Melanie started with
    starting_vacuum = remaining_cleaners + orange_cleaners

    # Display the number of vacuum starting with
    result = starting_vac

print(solution())