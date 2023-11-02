def solution():
    fudge_weight = 20
    fudge_price = 2.5
    truffles_quantity = 5 * 12  # 5 dozen
    truffles_price = 1.5
    pretzels_quantity = 3 * 12  # 3 dozen
    pretzels_price = 2.0

    # Calculate the total revenue from selling fudge
    fudge_revenue = fudge_weight * fudge_price

    # Calculate the total revenue from selling chocolate truffles
    truffles_revenue = truffles_quantity * truffles_price

    # Calculate the total revenue from selling chocolate-covered pretzels
    pretzels_revenue = pretzels_quantity * pretzels_price

    # Calculate the total revenue from selling all items
    total_revenue = fudge_revenue + truffles_revenue + pretzels_revenue
    result = total_revenue
    return result

print(solution())