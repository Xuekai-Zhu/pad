def solution():
    width = 5
    height = 4
    area = width * height * 2
    paint_coverage = 4 # in square feet
    paint_price = 2 # per quart

    # Calculate the total amount of paint needed
    paint_needed = area / paint_coverage

    # Calculate the total cost of all the paint that Tommy needs to buy
    total_paint_cost = paint_needed / 4 * paint_price # divided by 4 to convert to quarts

    result = total_paint_cost
    return result

print(solution())