def solution():
    mango_cost = 3  # Each mango costs $3
    apple_juice_cost = 3  # Each carton of apple juice costs $3
    mango_quantity = 6  # Rihanna bought 6 mangoes
    apple_juice_quantity = 6  # Rihanna bought 6 cartons of apple juice

    # Calculate the total cost of the mangoes and apple juice
    total_cost = (mango_cost * mango_quantity) + (apple_juice_cost * apple_juice_quantity)

    # Calculate the money Rihanna has left
    money_left = 50 - total_cost
    result = money_left
    return result

print(solution())