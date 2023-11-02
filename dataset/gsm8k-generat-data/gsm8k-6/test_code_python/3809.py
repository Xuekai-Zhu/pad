def solution():
    # Calculate the number of T-shirts and sweaters Norma left in the washer
    num_tshirts = 9
    num_sweaters = 2 * num_tshirts

    # Calculate the number of T-shirts and sweaters Norma finds missing
    missing_tshirts = 3 * 3  # Norma finds triple the number of original T-shirts missing
    missing_sweaters = num_sweaters - 3  # Norma finds 3 fewer sweaters remaining in the washer

    # Calculate the total number of missing items
    total_missing = missing_tshirts + missing_sweaters
    result = total_missing
    return result

print(solution())