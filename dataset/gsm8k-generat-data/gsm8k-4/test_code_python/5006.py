def solution():
    """James buys 3 packs of candy. He pays with a $20 bill and gets $11 change. How much did each pack of candy cost?"""
    # Define the total cost of the candy
    total_cost = 20 - 11

    # Calculate the cost per pack of candy
    cost_per_pack = total_cost / 3

    # Return the result
    result = cost_per_pack
    return result

print(solution())