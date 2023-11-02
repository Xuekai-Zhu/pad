def solution():
    initial_money = 20
    money_received = 2 * initial_money  # Faye's mother gave her twice as much as her money initially
    cupcakes = 10
    cost_per_cupcake = 1.5
    cookies = 5
    cost_per_cookie_box = 3

    # Calculate the total cost of cupcakes and cookies
    total_cost = cupcakes * cost_per_cupcake + cookies * cost_per_cookie_box

    # Calculate Faye's remaining money
    remaining_money = initial_money + money_received - total_cost
    result = remaining_money
    return result

print(solution())