def solution():
    num_balloons = 100
    water_per_balloon = 3  # ounces
    water_per_bottle = 50  # ounces
    cost_per_bottle = 2.5  # dollars
    num_dollars = 2
    num_cents = 100

    # Calculate the total amount of water needed in ounces
    total_water = num_balloons * water_per_balloon

    # Calculate the total number of bottles needed
    total_bottles = total_water / water_per_bottle

    # Calculate the total cost of all bottles of water needed
    total_cost = total_bottles * cost_per_bottle

    # Calculate the total amount of money Marcus has
    total_money = (num_dollars * 100) + num_cents

    # Calculate the change Marcus will receive
    change = total_money - total_cost
    result = change
    return result

print(solution())