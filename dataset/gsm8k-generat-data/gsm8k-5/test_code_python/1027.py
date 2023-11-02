def solution():
    # Calculate the cost of a black and white drawing
    bw_cost = 160

    # Calculate the cost of a color drawing
    color_cost = bw_cost * 1.5  # 50% more expensive than black and white

    # Calculate the total cost paid by John
    total_cost = color_cost

    result = total_cost
    return result

print(solution())