def solution():
    """To get free delivery, Alice needs to spend a minimum of $35.00 online at her favorite grocery store.  In her cart she has 1.5 pounds of chicken at $6.00 per pound, 1 pack of lettuce for $3.00, cherry tomatoes for $2.50, 4 sweet potatoes at $0.75 each, 2 heads of broccoli for $2.00 each and a pound of Brussel sprouts for $2.50.  How much more does she need to spend in order to get free delivery?"""
    # Define the prices of each item
    CHICKEN_PRICE = 6
    LETTUCE_PRICE = 3
    TOMATO_PRICE = 2.5
    POTATO_PRICE = 0.75
    BROCCOLI_PRICE = 2
    BRUSSEL_SPROUTS_PRICE = 2.5

    # Define the quantity of each item
    CHICKEN_QUANTITY = 1.5
    LETTUCE_QUANTITY = 1
    TOMATO_QUANTITY = 1
    POTATO_QUANTITY = 4
    BROCCOLI_QUANTITY = 2
    BRUSSEL_SPROUTS_QUANTITY = 1

    # Calculate the total cost of each item
    chicken_cost = CHICKEN_PRICE * CHICKEN_QUANTITY
    lettuce_cost = LETTUCE_PRICE * LETTUCE_QUANTITY
    tomato_cost = TOMATO_PRICE * TOMATO_QUANTITY
    potato_cost = POTATO_PRICE * POTATO_QUANTITY
    broccoli_cost = BROCCOLI_PRICE * BROCCOLI_QUANTITY
    sprouts_cost = BRUSSEL_SPROUTS_PRICE * BRUSSEL_SPROUTS_QUANTITY

    # Calculate the total cost of all the items
    total_cost = (chicken_cost + lettuce_cost + tomato_cost +
                  potato_cost + broccoli_cost + sprouts_cost)

    # Calculate how much more Alice needs to spend to get free delivery
    remaining_amount = max(35 - total_cost, 0)

    # Display the remaining amount needed for free delivery
    result = remaining_amount
    return result

print(solution())