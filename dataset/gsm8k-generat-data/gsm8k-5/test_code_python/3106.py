def solution():
    initial_arrival = 1000  # Initial arrival of 1000 kg of tomatoes
    sold_on_saturday = 300  # Sold 300 kg on Saturday
    tomatoes_remaining = initial_arrival - sold_on_saturday  # Tomatoes remaining after Saturday
    tomatoes_remaining -= 200  # 200 kg of tomatoes are thrown away on Sunday
    second_arrival = initial_arrival * 2  # Second shipment is twice the size of the first one
    total_tomatoes = tomatoes_remaining + second_arrival  # Total tomatoes ready for sale on Tuesday
    result = total_tomatoes
    return result

print(solution())