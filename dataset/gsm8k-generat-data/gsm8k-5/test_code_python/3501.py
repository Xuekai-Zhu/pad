def solution():
    num_plates = 9  # Chenny bought 9 plates
    plate_cost = 2  # Each plate costs $2
    total_plate_cost = num_plates * plate_cost  # Chenny spent this much on plates
    total_cost = 24  # Chenny spent a total of $24
    spoon_cost = 1.5  # Each spoon costs $1.50

    # Calculate how much Chenny spent on spoons
    total_spoon_cost = total_cost - total_plate_cost

    # Calculate how many spoons Chenny bought
    num_spoons = total_spoon_cost / spoon_cost
    result = num_spoons
    return result

print(solution())