def solution():
    num_plates = 9
    plate_price = 2

    total_plates_cost = num_plates * plate_price
    total_cost = 24
    spoon_price = 1.5

    # Calculate the cost of all spoons
    total_spoons_cost = total_cost - total_plates_cost

    # Calculate the number of spoons bought
    num_spoons = total_spoons_cost / spoon_price
    result = num_spoons
    return result

print(solution())