def solution():
    # First trip
    male_whales_trip1 = 28
    female_whales_trip1 = male_whales_trip1 * 2

    # Second trip
    baby_whales_trip2 = 8
    parent_whales_trip2 = baby_whales_trip2 * 2  # assuming each baby whale has two parents

    # Third trip
    male_whales_trip3 = male_whales_trip1 / 2
    female_whales_trip3 = female_whales_trip1

    # Calculate total number of whales
    total_whales = male_whales_trip1 + female_whales_trip1 + parent_whales_trip2 + male_whales_trip3 + female_whales_trip3

    result = total_whales
    return result

print(solution())