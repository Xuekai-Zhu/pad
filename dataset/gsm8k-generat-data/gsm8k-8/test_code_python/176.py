def solution():
    # Define the amount of sugar in one packet
    sugar_in_packet = 100/1000  # converted to kilograms

    # Calculate the total amount of sugar sold in one week
    total_sugar_sold = sugar_in_packet * 20

    result = total_sugar_sold
    return result

print(solution())