def solution():
    """Olivia gave William 10 napkins. Amelia also gives William twice the number of napkins Olivia gave him. If William had 15 napkins before, how many napkins does he have now?"""
    # Define the number of napkins Olivia gave
    olivia_napkins = 10

    # Define the multiplier for Amelia's napkins
    amelia_multiplier = 2

    # Define William's original number of napkins
    original_napkins = 15

    # Calculate the total number of napkins William has now
    total_napkins = original_napkins + olivia_napkins + (amelia_multiplier * olivia_napkins)

    # Display the total number of napkins William has now
    result = total_napkins
    return result

print(solution())