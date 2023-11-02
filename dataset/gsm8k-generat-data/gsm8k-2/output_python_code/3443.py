def solution():
    """Josie's mom gave her a $20 bill and asked her to go to the store for a few items. The list included a carton of milk for $4.00, a loaf of bread for $3.50, a box of laundry detergent for $10.25 and 2 pounds of bananas that were $0.75 per pound. Her mom also gave her a coupon for $1.25 off of the laundry detergent. At checkout, the clerk told her the milk was 1/2 off today. How much money did Josie have left over after she bought all of the groceries?"""
    total_cost = 0
    total_cost += 4.00  # milk
    total_cost += 3.50  # bread
    total_cost += 10.25  # laundry detergent
    total_cost += 2 * 0.75 * 0.5  # bananas (1/2 off)
    total_cost -= 1.25  # coupon for laundry detergent
    change = 20.00 - total_cost
    result = change
    return result

print(solution())