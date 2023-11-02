def solution():
    """Carrie is wrapping three birthday presents. One present needs two square feet of wrapping paper to cover. The second present needs three-quarters of that amount. The third present needs the same amount as both other presents put together. How many square feet of wrapping paper does Carrie need for all three presents?"""
    present1 = 2
    present2 = 0.75 * present1
    present3 = present1 + present2
    total_wrapping_paper = present1 + present2 + present3
    result = total_wrapping_paper
    return result

print(solution())