def solution():
    initial_money = 85  # cents
    mother_money = 40  # cents
    found_money = 50  # cents
    toy_cost = 160  # cents

    # Calculate the total amount of money Yanni has
    total_money = initial_money + mother_money + found_money

    # Calculate the amount of money Yanni spent on the toy
    spent_money = toy_cost

    # Calculate the amount of money Yanni has left
    left_money = total_money - spent_money
    result = left_money
    return result

print(solution())