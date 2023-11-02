def solution():
    """Melissa wants to make some dresses to sell at the upcoming festival. She has 56 square meters of fabric to make them. She knows that each dress takes 4 square meters of fabric and 3 hours to make. How many hours does she have to work?"""
    # Define the amount of fabric needed for each dress and the time it takes to make each dress
    FABRIC_PER_DRESS = 4
    TIME_PER_DRESS = 3

    # Define the total amount of fabric Melissa has to work with
    total_fabric = 56

    # Calculate the maximum number of dresses she can make
    max_dresses = total_fabric // FABRIC_PER_DRESS

    # Calculate the total time it will take to make all the dresses
    total_time = max_dresses * TIME_PER_DRESS

    # return the result
    result = total_time
    return result

print(solution())