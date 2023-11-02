def solution():
    num_tshirts_initial = 9
    num_sweaters_initial = num_tshirts_initial * 2

    num_sweaters_final = 3
    num_tshirts_final = num_sweaters_final * 3

    # Calculate the total number of items initially
    total_items_initial = num_tshirts_initial + num_sweaters_initial

    # Calculate the total number of items when Norma returns
    total_items_final = num_tshirts_final + num_sweaters_final

    # Calculate the number of missing items
    num_missing_items = total_items_initial - total_items_final
    result = num_missing_items
    return result

print(solution())