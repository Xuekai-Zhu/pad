def solution():
    sugar_per_packet = 100  # Each packet contains 100 grams of sugar
    packets_per_week = 20  # The store sells 20 packets of sugar every week

    # Calculate the total amount of sugar sold in a week, in grams
    total_sugar = sugar_per_packet * packets_per_week

    # Convert the total amount of sugar sold to kilograms
    sugar_in_kg = total_sugar / 1000
    result = sugar_in_kg
    return result

print(solution())