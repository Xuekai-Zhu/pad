def solution():
    """On a Sunday morning, Josephine sold milk in the farm stall. The buyers brought their containers. She filled three containers with two liters each, two containers with 0.75 liters each, and five containers with 0.5 liters each. How many liters of milk did Josephine sell in total?"""
    # Define the volume of milk in each type of container
    TWO_LITERS = 2
    THREE_QUARTERS_LITERS = 0.75
    HALF_LITERS = 0.5

    # Define the number of each type of container sold
    num_two_liters = 3
    num_three_quarters_liters = 2
    num_half_liters = 5

    # Calculate the total volume of milk sold
    total_volume = (num_two_liters * TWO_LITERS) + (num_three_quarters_liters * THREE_QUARTERS_LITERS) + (num_half_liters * HALF_LITERS)

    # Display the total volume of milk sold
    result = total_volume
    return result

print(solution())