def solution():
    # Define the initial amount of money
    initial_money = 20

    # Define the cost of the hat and pencil
    hat_cost = 10
    pencil_cost = 2

    # Calculate the total cost of the hat and pencil
    total_cost = hat_cost + pencil_cost

    # Define the cost of one cookie and the number of cookies purchased
    cookie_cost = 1.25
    num_cookies = 4

    # Calculate the total cost of the cookies
    cookie_total_cost = cookie_cost * num_cookies

    # Calculate the final amount of money Josh has left
    final_money = initial_money - total_cost - cookie_total_cost

    result = final_money
    return result

print(solution())