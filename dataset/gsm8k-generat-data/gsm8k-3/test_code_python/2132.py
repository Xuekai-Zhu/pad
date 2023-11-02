def solution():
    """The basketball team sold 50 cupcakes for $2 each and 40 cookies for $0.5 each. Then the money from their sales was used to buy two basketballs that cost $40 each. The rest of the money was used to buy 20 bottles of energy drinks. How much does a bottle of energy drink cost?"""
    # Define the prices and quantities of cupcakes and cookies
    CUPCAKE_PRICE = 2
    COOKIE_PRICE = 0.5
    CUPCAKE_QUANTITY = 50
    COOKIE_QUANTITY = 40

    # Calculate the total revenue from cupcake and cookie sales
    cupcake_sales = CUPCAKE_PRICE * CUPCAKE_QUANTITY
    cookie_sales = COOKIE_PRICE * COOKIE_QUANTITY
    total_sales = cupcake_sales + cookie_sales

    # Calculate the cost of the basketballs
    basketball_cost = 2 * 40

    # Calculate the remaining amount of money
    remaining_money = total_sales - basketball_cost

    # Calculate the cost per bottle of energy drink
    energy_drink_cost = remaining_money / 20

    # Display the cost per bottle of energy drink
    result = energy_drink_cost
    return result

print(solution())