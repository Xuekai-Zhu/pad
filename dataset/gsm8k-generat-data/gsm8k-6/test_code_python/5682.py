def solution():
    # Calculate the total amount earned from the sale of the suits
    total_suit_cost = 2 * 700

    # Calculate the total amount earned from the sale of the shirts
    total_shirt_cost = 6 * 50

    # Calculate the total amount earned from the sale of the loafers
    total_loafer_cost = 2 * 150

    # Calculate the total amount of money earned from sales
    total_sales = total_suit_cost + total_shirt_cost + total_loafer_cost

    # Calculate the commission earned by Enrique
    commission = 0.15 * total_sales
    result = commission
    return result

print(solution())