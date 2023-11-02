def solution():
    """Nida has 50 chocolates in which some are in 3 filled boxes and 5 pieces are not in a box. Her friend brought 25 pieces of chocolates. If all chocolates must be placed in a box, how many more boxes do they need?"""
    # Define the initial number of chocolates and boxes
    initial_chocolates = 50
    initial_boxes = 3

    # Calculate the number of chocolates not in a box
    unboxed_chocolates = 5

    # Calculate the total number of chocolates
    total_chocolates = initial_chocolates + unboxed_chocolates

    # Calculate the number of boxes needed for all the chocolates
    total_boxes = (total_chocolates // 25) + (1 if total_chocolates % 25 != 0 else 0)

    # Calculate the additional boxes needed
    additional_boxes = total_boxes - initial_boxes

    # Return the result
    result = additional_boxes
    return result

print(solution())