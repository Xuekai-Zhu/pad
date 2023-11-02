def solution():
    total_money = 71
    num_shirts = 5
    shirt_price = 5
    pants_price = 26

    # Calculate the total cost of all shirts
    total_shirts_cost = num_shirts * shirt_price

    # Calculate the total cost of the pants
    total_pants_cost = pants_price

    # Calculate the total cost of all clothes
    total_clothes_cost = total_shirts_cost + total_pants_cost

    # Calculate the remaining money after buying all clothes
    remaining_money = total_money - total_clothes_cost
    result = remaining_money
    return result

print(solution())