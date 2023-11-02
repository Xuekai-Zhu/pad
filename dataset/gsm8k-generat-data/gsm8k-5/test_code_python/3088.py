def solution():
    distance_per_gasoline = 40  # Keanu's motorcycle consumes 8 liters of gasoline per 40 miles
    total_distance = 280 * 2  # Keanu is making a round trip, so he will travel 280 miles twice
    total_gasoline_needed = (total_distance / distance_per_gasoline) * 8  # Calculate total gasoline needed for the round trip

    # Calculate how many times Keanu needs to refill his motorcycle
    num_refills = total_gasoline_needed // 8
    if total_gasoline_needed % 8 != 0:
        num_refills += 1

    result = int(num_refills)
    return result

print(solution())