def solution():
    # Calculate the total cost of the lollipops
    lollipop_cost = 4 * 2

    # Calculate the cost of one pack of chocolate
    chocolate_cost = 4 * 2

    # Calculate the total cost of the chocolate
    total_chocolate_cost = 6 * chocolate_cost

    # Calculate the total cost of the purchase
    total_purchase_cost = lollipop_cost + total_chocolate_cost

    # Calculate the amount of money Blake gave the cashier
    money_given = 6 * 10

    # Calculate the change Blake will get back
    change = money_given - total_purchase_cost
    result = change
    return result

print(solution())