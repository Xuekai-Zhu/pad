def solution():
    initial_money = 20
    mother_money = initial_money * 2
    cupcakes_price = 1.5
    num_cupcakes = 10
    cookies_price = 3
    num_cookies = 5

    # Calculate total money
    total_money = initial_money + mother_money

    # Calculate total spent on cupcakes
    cupcakes_cost = cupcakes_price * num_cupcakes

    # Calculate total spent on cookies
    cookies_cost = cookies_price * num_cookies

    # Calculate total spent
    total_spent = cupcakes_cost + cookies_cost

    # Calculate left money
    left_money = total_money - total_spent
    result = left_money
    return result

print(solution())