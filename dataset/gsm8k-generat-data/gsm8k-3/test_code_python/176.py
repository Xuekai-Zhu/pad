def solution():
    """A store sells 20 packets of 100 grams of sugar every week. How many kilograms of sugar does it sell every week?"""
    # Define the weight of a packet of sugar in grams
    packet_weight = 100

    # Define the number of packets sold every week
    packets_sold = 20

    # Calculate the total weight of sugar sold every week in grams
    total_weight = packet_weight * packets_sold

    # Convert the total weight to kilograms
    total_weight_kg = total_weight / 1000

    # Return the result
    result = total_weight_kg
    return result

print(solution())