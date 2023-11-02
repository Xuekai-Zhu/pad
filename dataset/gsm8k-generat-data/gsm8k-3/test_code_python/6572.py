def solution():
    """Josh’s mom gives him $20 to go shopping at the mall. He buys a hat for $10 and a pencil for $2. Then he buys four cookies. If each cookie costs $1.25, how much money does Josh have left?"""
    # Define the initial amount of money Josh has
    initial_money = 20

    # Define the cost of the hat and pencil
    hat_cost = 10
    pencil_cost = 2

    # Define the number of cookies Josh buys and the cost per cookie
    cookie_count = 4
    cookie_cost = 1.25

    # Calculate the total cost of the hat, pencil, and cookies
    total_cost = hat_cost + pencil_cost + (cookie_count * cookie_cost)

    # Calculate the amount of money Josh has left
    money_left = initial_money - total_cost

    # Display the amount of money Josh has left
    result = money_left
    return result

print(solution())