def solution():
    num_packets = 150
    ml_per_packet = 250
    ml_per_ounce = 30

    # Calculate the total volume of milk in ml
    total_ml = num_packets * ml_per_packet

    # Convert ml to fluid ounces
    total_ounces = total_ml / ml_per_ounce
    result = total_ounces
    return result

print(solution())