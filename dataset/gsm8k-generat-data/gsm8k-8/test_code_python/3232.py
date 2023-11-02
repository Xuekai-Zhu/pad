def solution():
    # Calculate Mr. Grey's selling price
    grey_profit = 0.1 * 100000
    grey_selling_price = 100000 + grey_profit

    # Calculate Mr. Brown's buying price
    brown_buying_price = grey_selling_price

    # Calculate Mr. Brown's selling price
    brown_loss = 0.1 * brown_buying_price
    brown_selling_price = brown_buying_price - brown_loss
    result = brown_selling_price
    return result

print(solution())