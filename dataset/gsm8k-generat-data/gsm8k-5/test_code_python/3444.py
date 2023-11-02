def solution():
    money_given = 20  # Josie's mom gave her a $20 bill
    milk_price = 4.00  # Milk costs $4.00
    bread_price = 3.50  # Bread costs $3.50
    detergent_price = 10.25  # Detergent costs $10.25
    bananas_price = 0.75  # Bananas cost $0.75 per pound
    bananas_weight = 2  # Josie bought 2 pounds of bananas
    detergent_coupon = 1.25  # Josie had a $1.25 coupon for the detergent

    # Calculate the total cost of the items before discounts or coupons
    total_cost = milk_price + bread_price + detergent_price + (bananas_price * bananas_weight)

    # Apply discounts and coupons
    total_cost -= 2  # Milk is 1/2 off today, so its cost is reduced by $2.00
    total_cost -= detergent_coupon  # Josie used the $1.25 coupon for the detergent

    # Calculate how much money Josie has left after buying the groceries
    money_left = money_given - total_cost
    result = money_left
    return result

print(solution())