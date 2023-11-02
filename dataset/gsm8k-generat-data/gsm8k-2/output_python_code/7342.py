def solution():
    """At the bake sale, Tamara makes $32 from the brownies. She made 2 pans of brownies which were all sold. The brownies were cut into 8 big square pieces. How much did each brownie cost?"""
    total_income = 32
    num_pans = 2
    num_pieces = num_pans * 8
    cost_per_brownie = total_income / num_pieces
    result = cost_per_brownie
    return result

print(solution())