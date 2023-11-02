def solution():
    packets = 150  # The shopkeeper bought 150 packets of milk
    volume_per_packet = 250  # Each packet contained 250 ml of milk
    ml_total = packets * volume_per_packet  # Calculate the total volume in ml

    # Convert ml to fluid ounces
    ounces_total = ml_total / 30

    result = ounces_total
    return result

print(solution())