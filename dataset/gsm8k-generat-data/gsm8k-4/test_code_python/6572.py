def solution():
    """Josh’s mom gives him $20 to go shopping at the mall. He buys a hat for $10 and a pencil for $2. Then he buys four cookies. If each cookie costs $1.25, how much money does Josh have left?"""
    # Define the initial amount of money Josh has
    initial_money = 20

    # Define the cost of the hat and pencil
    hat_cost = 10
    pencil_cost = 2

    # Define the number of cookies and the cost per cookie
    num_cookies = 4
    cookie_cost = 1.25

    # Calculate the total amount spent
    total_spent = hat_cost + pencil_cost + (num_cookies * cookie_cost)

    # Calculate the amount left
    money_left = initial_money - total_spent

    # return the result 
    result = money_left
    return result

print(solution())