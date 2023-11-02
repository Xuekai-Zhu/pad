def solution():
    # Define the number of total units and the number of defective units
    total_units = 20
    defective_units = 5

    # Calculate the number of non-defective units
    non_defective_units = total_units - defective_units

    # Calculate the number of units sold to customers A and C
    sold_to_A = 3
    sold_to_C = 7

    # Calculate the number of units sold to customer B
    sold_to_B = non_defective_units - sold_to_A - sold_to_C
    result = sold_to_B
    return result

print(solution())