def solution():
    # Define the menu prices
    salisbury_steak_price = 16.00
    chicken_fried_steak_price = 18.00

    # Calculate the discounted prices during the Early Bird Dinner
    salisbury_steak_discounted_price = 0.5 * salisbury_steak_price
    chicken_fried_steak_discounted_price = 0.5 * chicken_fried_steak_price

    # Calculate the total bill
    total_bill = salisbury_steak_discounted_price + chicken_fried_steak_discounted_price

    result = total_bill
    return result

print(solution())