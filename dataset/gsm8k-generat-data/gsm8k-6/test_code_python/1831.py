def solution():
    # Calculate the total number of pencils and pens ordered
    num_pencils = 15 * 80  # 15 boxes each containing 80 pencils
    num_pens = (2 * num_pencils) + 300  # 300 more than twice as many pens as pencils

    # Calculate the total cost of pencils and pens
    total_cost = (num_pencils * 4) + (num_pens * 5)  # each pencil costs $4 and each pen costs $5

    result = total_cost
    return result

print(solution())