def solution():
    """Olivia gave William 10 napkins. Amelia also gives William twice the number of napkins Olivia gave him. If William had 15 napkins before, how many napkins does he have now?"""
    # Define the number of napkins initially owned by William
    initial_napkins = 15

    # Define the number of napkins Olivia gave William
    olivia_napkins = 10

    # Define the number of napkins Amelia gave William
    amelia_napkins = olivia_napkins * 2

    # Calculate the total number of napkins William has now
    total_napkins = initial_napkins + olivia_napkins + amelia_napkins

    # return the result
    result = total_napkins
    return result

print(solution())