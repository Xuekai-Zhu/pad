def solution():
    menu_price_salisbury = 16.00  # Menu price of Salisbury Steak
    menu_price_chicken_fried = 18.00  # Menu price of Chicken Fried Steak
    discount = 0.5  # Early Bird Dinner discount rate
    discount_price_salisbury = menu_price_salisbury * discount  # Discounted price of Salisbury Steak
    discount_price_chicken_fried = menu_price_chicken_fried * discount  # Discounted price of Chicken Fried Steak
    total_bill = discount_price_salisbury + discount_price_chicken_fried  # Total bill for both meals
    result = total_bill
    return result

print(solution())