def solution():
    weight_per_plate = 30  # Each weight plate weighs 30 pounds
    num_plates = 10  # Tom uses 10 weight plates
    added_weight = 0.2  # The machine adds 20% more weight on the lowering portion

    # Calculate the total weight of the plates
    total_weight = weight_per_plate * num_plates

    # Calculate the weight added by the machine
    added_weight_amount = total_weight * added_weight

    # Calculate the total weight felt on the lowering portion
    total_weight_felt = total_weight + added_weight_amount
    result = total_weight_felt
    return result

print(solution())