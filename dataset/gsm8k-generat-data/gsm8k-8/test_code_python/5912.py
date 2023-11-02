def solution():
    # Define the prices of each item
    sandwich_price = 2
    hamburger_price = 2
    hotdog_stick_price = 1
    fruit_juice_price = 2

    # Calculate Selene's total cost
    selene_cost = 3 * sandwich_price + fruit_juice_price

    # Calculate Tanya's total cost
    tanya_cost = 2 * hamburger_price + 2 * fruit_juice_price

    # Calculate the total cost for Selene and Tanya
    total_cost = selene_cost + tanya_cost
    result = total_cost
    return result

print(solution())