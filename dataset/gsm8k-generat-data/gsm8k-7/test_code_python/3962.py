def solution():
    num_avocados = 3
    avocado_price = 2
    money = 20

    # Calculate the total cost of all avocados
    total_avocado_cost = num_avocados * avocado_price

    # Calculate the amount of change that Lucas receives
    change = money - total_avocado_cost
    result = change
    return result

print(solution())