def solution():
    laptops_price = 600
    smartphones_price = 400
    num_laptops = 2
    num_smartphones = 4

    # Calculate the total cost of the laptops and smartphones
    total_cost = (laptops_price * num_laptops) + (smartphones_price * num_smartphones)

    # Calculate the amount of change Celine will get back
    change = 3000 - total_cost
    result = change
    return result

print(solution())