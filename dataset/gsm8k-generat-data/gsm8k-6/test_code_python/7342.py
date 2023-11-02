def solution():
    price_per_shirt = 10  # all shirts are $10
    total_price = 3 * price_per_shirt  # total price of 3 shirts without discounts
    price_with_discounts = 10 + (0.5 * price_per_shirt) + (0.4 * price_per_shirt)  # price of 3 shirts with discounts applied
    money_saved = total_price - price_with_discounts  # calculate the difference between original price and discounted price
    result = money_saved
    return result

print(solution())