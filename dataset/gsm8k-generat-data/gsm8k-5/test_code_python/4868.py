def solution():
    # Calculate the number of whales on the first trip
    male_whales_first_trip = 28
    female_whales_first_trip = 2 * male_whales_first_trip
    total_whales_first_trip = male_whales_first_trip + female_whales_first_trip

    # Calculate the number of whales on the second trip
    baby_whales_second_trip = 8
    parent_whales_second_trip = baby_whales_second_trip * 2
    total_whales_second_trip = baby_whales_second_trip + parent_whales_second_trip

    # Calculate the number of whales on the third trip
    male_whales_third_trip = 0.5 * male_whales_first_trip
    female_whales_third_trip = female_whales_first_trip
    total_whales_third_trip = male_whales_third_trip + female_whales_third_trip

    # Calculate the total number of whales seen
    total_whales = total_whales_first_trip + total_whales_second_trip + total_whales_third_trip
    result = total_whales
    return result

print(solution())