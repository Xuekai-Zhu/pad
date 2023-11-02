def solution():
    initial_money = 20
    money_from_mother = 2 * initial_money

    cupcakes_cost = 10 * 1.5
    cookies_cost = 5 * 3

    total_cost = cupcakes_cost + cookies_cost

    remaining_money = money_from_mother - total_cost
    result = remaining_money
    return result

print(solution())