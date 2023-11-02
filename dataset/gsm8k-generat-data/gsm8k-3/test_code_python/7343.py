def solution():
    """At the bake sale, Tamara makes $32 from the brownies. She made 2 pans of brownies which were all sold.  The brownies were cut into 8 big square pieces.  How much did each brownie cost?"""
    # Define the number of pans of brownies and the total amount earned
    NUM_PANS = 2
    TOTAL_EARNED = 32

    # Calculate the total number of brownies sold
    total_brownies = NUM_PANS * 8

    # Calculate the cost per brownie
    cost_per_brownie = TOTAL_EARNED / total_brownies

    # Display the cost per brownie
    result = cost_per_brownie
    return result

print(solution())