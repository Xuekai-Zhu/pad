def solution():
    """Josie's mom gave her a $20 bill and asked her to go to the store for a few items.  The list included a carton of milk for $4.00, a loaf of bread for $3.50, a box of laundry detergent for $10.25 and 2 pounds of bananas that were $0.75 per pound.  Her mom also gave her a coupon for $1.25 off of the laundry detergent.  At checkout, the clerk told her the milk was 1/2 off today.  How much money did Josie have left over after she bought all of the groceries?"""
    # Define the cost of each item
    MILK_PRICE = 4.00
    BREAD_PRICE = 3.50
    DETERGENT_PRICE = 10.25
    BANANAS_PRICE = 0.75

    # Define the quantity of each item
    milk_quantity = 1
    bread_quantity = 1
    detergent_quantity = 1
    bananas_quantity = 2

    # Calculate the total cost of each item
    milk_cost = MILK_PRICE * 0.5
    bread_cost = BREAD_PRICE
    detergent_cost = DETERGENT_PRICE - 1.25
    bananas_cost = BANANAS_PRICE * bananas_quantity

    # Calculate the total cost of all the items
    total_cost = milk_cost + bread_cost + detergent_cost + bananas_cost

    # Calculate the amount of money Josie has left over
    money_left = 20 - total_cost

    # Display the amount of money Josie has left over
    result = money_left
    return result

print(solution())