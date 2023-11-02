def solution():
    """Josie's mom gave her a $20 bill and asked her to go to the store for a few items. The list included a carton of milk for $4.00, a loaf of bread for $3.50, a box of laundry detergent for $10.25 and 2 pounds of bananas that were $0.75 per pound. Her mom also gave her a coupon for $1.25 off of the laundry detergent. At checkout, the clerk told her the milk was 1/2 off today. How much money did Josie have left over after she bought all of the groceries?"""
    # Define the prices of the items
    milk_price = 4.00
    bread_price = 3.50
    detergent_price = 10.25
    bananas_price = 0.75

    # Apply the discounts and calculate the total cost
    milk_price *= 0.5
    total_cost = milk_price + bread_price + detergent_price - 1.25 + (2 * bananas_price)

    # Calculate the amount of change
    change = 20 - total_cost

    result = round(change, 2)
    return result

print(solution())