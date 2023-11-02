def solution():
    """Ishmael was monitoring whales out at sea for conservation purposes. Each time he takes a trip to sea, he sees a different group of whales. On his first trip, he counts 28 male whales and twice as many female whales. On his second trip, he sees 8 baby whales, each travelling with their parents. On his third trip, he counts half as many male whales as the first trip and the same number of female whales as on the first trip. In total, how many whales were out at sea during Ishmael’s monitoring?"""
    # Calculate the number of female whales on the first trip
    female_whales_first_trip = 2 * 28

    # Calculate the number of whales (including parents) on the second trip
    whales_second_trip = 8 * 3

    # Calculate the number of male whales on the third trip
    male_whales_third_trip = 28 / 2

    # Calculate the total number of whales
    total_whales = 28 + female_whales_first_trip + whales_second_trip + male_whales_third_trip + female_whales_first_trip

    # Return the result
    result = total_whales
    return result

print(solution())