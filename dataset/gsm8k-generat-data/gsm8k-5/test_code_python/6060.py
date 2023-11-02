def solution():
    joy_pencils = 30  # Joy has 30 pencils
    colleen_pencils = 50  # Colleen has 50 pencils
    pencil_price = 4  # Each pencil costs $4

    # Calculate the total amount paid by Joy for her pencils
    joy_total_cost = joy_pencils * pencil_price

    # Calculate the total amount paid by Colleen for her pencils
    colleen_total_cost = colleen_pencils * pencil_price

    # Calculate how much more Colleen paid than Joy for her pencils
    difference = colleen_total_cost - joy_total_cost
    result = difference
    return result

print(solution())