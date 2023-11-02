def solution():
    pens = 2 * pencils  # The number of pens is twice the number of pencils
    total_items = pencils + pens + 1  # There is also one eraser
    total_items = 13  # Tommy has 13 items in his pencil case

    # Solve for the number of pencils
    pencils = (total_items - 1) / 3
    result = pencils
    return result

print(solution())