def solution():
    # Define variables
    current_price = 20.00
    tariff_increase = 0.25
    num_bottles = 5

    # Calculate new price after tariff increase
    new_price = current_price * (1 + tariff_increase)

    # Calculate total cost increase for 5 bottles
    cost_increase = (new_price - current_price) * num_bottles

    result = round(cost_increase, 2)
    return result

print(solution())