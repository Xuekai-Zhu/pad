def solution():
    # Calculate the total area of the wall to be covered by 2 coats of paint
    total_area = 600 * 2  # two coats of paint

    # Calculate the number of gallon cans of paint Linda needs to buy
    num_cans = total_area / 400  # one can of paint can cover 400 sq. ft.
    result = num_cans
    return result

print(solution())