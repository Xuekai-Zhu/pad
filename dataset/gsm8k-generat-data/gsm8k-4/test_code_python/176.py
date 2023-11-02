def solution():
    """A store sells 20 packets of 100 grams of sugar every week. How many kilograms of sugar does it sell every week?"""
    # Define the weight of each packet in grams
    packet_weight = 100

    # Define the number of packets sold each week
    packets_sold = 20

    # Calculate the total weight sold in grams
    total_weight = packet_weight * packets_sold

    # Convert the total weight to kilograms
    kg_sold = total_weight / 1000

    # return the result
    result = kg_sold
    return result

print(solution())