def solution():
    # Calculate the total amount of money made by the candy store
    fudge_sales = 20 * 2.5  # 20 pounds of fudge sold at $2.50/pound
    truffle_sales = 5 * 12 * 1.5  # 5 dozen chocolate truffles sold at $1.50 each
    pretzel_sales = 3 * 12 * 2  # 3 dozen chocolate-covered pretzels sold at $2.00 each
    total_sales = fudge_sales + truffle_sales + pretzel_sales
    result = total_sales
    return result

print(solution())