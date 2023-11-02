def solution():
    total_doughnuts = 300  # The bakery makes 300 doughnuts
    doughnuts_per_box = 10  # Each box of doughnuts holds 10 doughnuts
    sold_boxes = 27  # The bakery sells 27 boxes of doughnuts

    # Calculate the total number of doughnuts sold
    sold_doughnuts = sold_boxes * doughnuts_per_box

    # Calculate the number of doughnuts left over
    left_over = total_doughnuts - sold_doughnuts

    result = left_over
    return result

print(solution())