def solution():
    """Melissa wants to make some dresses to sell at the upcoming festival. She has 56 square meters of fabric to make them. She knows that each dress takes 4 square meters of fabric and 3 hours to make. How many hours does she have to work?"""
    # Define the amount of fabric needed and time required to make one dress
    FABRIC_PER_DRESS = 4
    TIME_PER_DRESS = 3

    # Define the total amount of fabric available
    total_fabric = 56

    # Calculate the maximum number of dresses that can be made with the available fabric
    max_dresses = total_fabric // FABRIC_PER_DRESS

    # Calculate the amount of time required to make the maximum number of dresses
    total_time = max_dresses * TIME_PER_DRESS

    # Display the total amount of time required
    result = total_time
    return result

print(solution())