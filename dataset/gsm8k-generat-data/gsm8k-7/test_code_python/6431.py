def solution():
    computer_cost = 700
    accessories_cost = 200
    playstation_value = 400
    playstation_discount = 0.20 # 20% discount

    # Calculate the amount John sold his PlayStation for
    playstation_sold = playstation_value * (1 - playstation_discount)

    # Calculate the total cost of the computer and accessories
    total_cost = computer_cost + accessories_cost

    # Calculate the amount of money that came out of John's pocket
    out_of_pocket = total_cost - playstation_sold
    result = out_of_pocket
    return result

print(solution())