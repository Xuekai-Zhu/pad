def solution():
    # Calculate the remaining amount of tomatoes after each day
    remaining_tomatoes = 1000 - 300 - 200  # Friday shipment minus Saturday sales minus Sunday waste
    remaining_tomatoes += 2*1000  # Monday shipment is twice as big as Friday's

    # Marta has the remaining tomatoes ready for sale on Tuesday
    result = remaining_tomatoes
    return result

print(solution())