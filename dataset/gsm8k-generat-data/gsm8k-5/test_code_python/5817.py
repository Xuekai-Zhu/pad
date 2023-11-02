def solution():
    # Calculate the total sale from neighborhood A
    total_sale_A = 10 * 2 * 2  # 10 homes, 2 boxes per home, $2 per box

    # Calculate the total sale from neighborhood B
    total_sale_B = 5 * 5 * 2  # 5 homes, 5 boxes per home, $2 per box

    # Determine the better choice of neighborhood
    if total_sale_A > total_sale_B:
        better_neighborhood_sale = total_sale_A
    else:
        better_neighborhood_sale = total_sale_B

    result = better_neighborhood_sale
    return result

print(solution())