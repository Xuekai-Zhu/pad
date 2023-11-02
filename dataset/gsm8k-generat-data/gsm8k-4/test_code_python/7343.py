def solution():
    """At the bake sale, Tamara makes $32 from the brownies. She made 2 pans of brownies which were all sold. The brownies were cut into 8 big square pieces. How much did each brownie cost?"""
    # Define the number of pans
    num_pans = 2

    # Calculate the total number of brownies
    num_brownies = num_pans * 8

    # Calculate the cost per brownie
    cost_per_brownie = 32 / num_brownies

    result = round(cost_per_brownie, 2)
    return result

print(solution())