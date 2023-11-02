def solution():
    budget = 50
    num_black_inks = 2
    black_ink_price = 11
    num_red_inks = 3
    red_ink_price = 15
    num_yellow_inks = 2
    yellow_ink_price = 13

    # Calculate the total cost of all black inks
    total_black_ink_cost = num_black_inks * black_ink_price

    # Calculate the total cost of all red inks
    total_red_ink_cost = num_red_inks * red_ink_price

    # Calculate the total cost of all yellow inks
    total_yellow_ink_cost = num_yellow_inks * yellow_ink_price

    # Calculate the total cost of all inks
    total_cost = total_black_ink_cost + total_red_ink_cost + total_yellow_ink_cost

    # Calculate the amount of money Phantom needs to buy all the inks
    extra_money = total_cost - budget
    result = extra_money
    return result

print(solution())