def solution():
    """On Tuesday, 12,000 ice cream cones were sold. On Wednesday, the number of ice cream cones sold was double the amount sold on Tuesday. How many ice cream cones have been sold in total?"""
    tuesday_sales = 12000
    wednesday_sales = 2 * tuesday_sales
    total_sales = tuesday_sales + wednesday_sales
    result = total_sales
    return result

print(solution())