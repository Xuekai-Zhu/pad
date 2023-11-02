def solution():
    # Calculate total initial money Yanni had
    initial_money = 85  # in cents
    mother_money = 40  # in cents
    found_money = 50  # in cents
    total_money = initial_money + mother_money + found_money

    # Calculate remaining money after buying the toy
    toy_cost = 160  # in cents
    remaining_money = total_money - toy_cost

    result = remaining_money  # answer is in cents
    return result

print(solution())